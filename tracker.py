import os
import re
import csv
from datetime import datetime

def get_last_modified(path):
    if not os.path.exists(path):
        return None
    timestamp = os.path.getmtime(path)
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M')

def track_assignments(base_dir):
    submissions_dir = os.path.join(base_dir, "submissions")
    if not os.path.exists(submissions_dir):
        print(f"Error: Submissions directory not found at {submissions_dir}")
        return

    students = {}
    
    # Stricter regex patterns
    a1_regex = re.compile(r"^(assig[n]*m[er]*nt|asig[n]*ment|a1|research|lesson[-_ ]*one)[-_ ]*(1|one|one\.md)?$", re.IGNORECASE)
    a2_regex = re.compile(r"^(assig[n]*m[er]*nt|asig[n]*ment|a2|project|lesson[-_ ]*two)[-_ ]*(2|two)?$", re.IGNORECASE)
    a3_regex = re.compile(r"^(assig[n]*m[er]*nt|asig[n]*ment|a3|lesson[-_ ]*three)[-_ ]*(3|three)?$", re.IGNORECASE)

    sub_a1_regex = re.compile(r"(assig[n]*m[er]*nt|asig[n]*ment)[-_ ]*(1|one)", re.IGNORECASE)
    sub_a2_regex = re.compile(r"(assig[n]*m[er]*nt|asig[n]*ment)[-_ ]*(2|two)", re.IGNORECASE)
    sub_a3_regex = re.compile(r"(assig[n]*m[er]*nt|asig[n]*ment)[-_ ]*(3|three)", re.IGNORECASE)

    exclude_folders = {"000.example", ".git", "assignment-1", "assignment-2", "assignment-3"}

    # Get all possible students (all folders in submissions excluding noise)
    all_folders = [f for f in os.listdir(submissions_dir) if os.path.isdir(os.path.join(submissions_dir, f)) and f.lower() not in exclude_folders]

    for student_name in all_folders:
        item_path = os.path.join(submissions_dir, student_name)
        
        students[student_name] = {
            "A1": {"status": False, "evidence": "", "date": "N/A"}, 
            "A2": {"status": False, "evidence": "", "date": "N/A"}, 
            "A3": {"status": False, "evidence": "", "date": "N/A"}
        }
        
        for root, dirs, files in os.walk(item_path):
            depth = root[len(item_path):].count(os.sep)
            if depth > 2:
                continue
            
            # Check directory names
            for d in dirs:
                d_path = os.path.join(root, d)
                if a1_regex.match(d) or sub_a1_regex.search(d):
                    if not students[student_name]["A1"]["status"]:
                        students[student_name]["A1"] = {"status": True, "evidence": d, "date": get_last_modified(d_path)}
                if a2_regex.match(d) or sub_a2_regex.search(d):
                    if not students[student_name]["A2"]["status"]:
                        students[student_name]["A2"] = {"status": True, "evidence": d, "date": get_last_modified(d_path)}
                if a3_regex.match(d) or sub_a3_regex.search(d):
                    if not students[student_name]["A3"]["status"]:
                        students[student_name]["A3"] = {"status": True, "evidence": d, "date": get_last_modified(d_path)}
            
            # Check filenames
            for f in files:
                f_path = os.path.join(root, f)
                cleanup_name = f.lower()
                if "readme" in cleanup_name or cleanup_name.startswith("."):
                    continue
                    
                if sub_a1_regex.search(f):
                    if not students[student_name]["A1"]["status"]:
                        students[student_name]["A1"] = {"status": True, "evidence": f, "date": get_last_modified(f_path)}
                if sub_a2_regex.search(f):
                    if not students[student_name]["A2"]["status"]:
                        students[student_name]["A2"] = {"status": True, "evidence": f, "date": get_last_modified(f_path)}
                if sub_a3_regex.search(f):
                    if not students[student_name]["A3"]["status"]:
                        students[student_name]["A3"] = {"status": True, "evidence": f, "date": get_last_modified(f_path)}
    
    generate_reports(base_dir, students)

def generate_reports(base_dir, students):
    # Valid students have at least one submission
    valid_students = {k: v for k, v in students.items() if any(a["status"] for a in v.values())}
    # Missing students have zero submissions
    missing_students = {k: v for k, v in students.items() if not any(a["status"] for a in v.values())}
    
    total_valid = len(valid_students)
    count_a1 = sum(1 for s in valid_students.values() if s["A1"]["status"])
    count_a2 = sum(1 for s in valid_students.values() if s["A2"]["status"])
    count_a3 = sum(1 for s in valid_students.values() if s["A3"]["status"])
    
    # 1. Generate Markdown Report
    md_path = os.path.join(base_dir, "TRACKER.md")
    with open(md_path, "w") as f:
        f.write("# Student Assignment Tracker Report\n\n")
        f.write(f"**Total Students Found:** {len(students)}\n")
        f.write(f"**Students with Submissions:** {total_valid}\n")
        f.write(f"**Students with Zero Submissions:** {len(missing_students)}\n\n")
        
        f.write("| Assignment | Submissions |\n")
        f.write("| --- | --- |\n")
        f.write(f"| Assignment 1 | {count_a1} |\n")
        f.write(f"| Assignment 2 | {count_a2} |\n")
        f.write(f"| Assignment 3 | {count_a3} |\n\n")
        
        f.write("## Detailed Submission List (Evidence & Date)\n\n")
        f.write("| Student Name | A1 | A1 Date | A2 | A2 Date | A3 | A3 Date |\n")
        f.write("| --- | --- | --- | --- | --- | --- | --- |\n")
        
        for student in sorted(valid_students.keys()):
            s = valid_students[student]
            a1 = f"✅ ({s['A1']['evidence']})" if s["A1"]["status"] else "❌"
            a2 = f"✅ ({s['A2']['evidence']})" if s["A2"]["status"] else "❌"
            a3 = f"✅ ({s['A3']['evidence']})" if s["A3"]["status"] else "❌"
            f.write(f"| {student} | {a1} | {s['A1']['date']} | {a2} | {s['A2']['date']} | {a3} | {s['A3']['date']} |\n")
            
        if missing_students:
            f.write("\n## Students with zero submissions\n\n")
            for student in sorted(missing_students.keys()):
                f.write(f"- {student}\n")

    # 2. Generate CSV Report
    csv_path = os.path.join(base_dir, "TRACKER.csv")
    with open(csv_path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Student Name", "A1 Status", "A1 Evidence", "A1 Date", "A2 Status", "A2 Evidence", "A2 Date", "A3 Status", "A3 Evidence", "A3 Date"])
        for student in sorted(students.keys()):
            s = students[student]
            writer.writerow([
                student,
                "Submitted" if s["A1"]["status"] else "Missing", s["A1"]["evidence"], s["A1"]["date"],
                "Submitted" if s["A2"]["status"] else "Missing", s["A2"]["evidence"], s["A2"]["date"],
                "Submitted" if s["A3"]["status"] else "Missing", s["A3"]["evidence"], s["A3"]["date"]
            ])
            
    print(f"Reports generated: {md_path} and {csv_path}")

if __name__ == "__main__":
    current_dir = os.path.abspath(os.path.dirname(__file__))
    track_assignments(current_dir)
