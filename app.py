from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initial data grounded in Ghanaian SME & Youth context
opportunities = [
    {
        "id": "task-101",
        "title": "Setup Google Business & Basic Product Catalog",
        "company": "Accra Artisans Collective",
        "location": "Greater Accra / Remote",
        "category": "Tech",
        "stipend": "GH₵ 400 + Badge",
        "duration": "2 Weeks",
        "description": "Help an artisanal leather works collective in Osu establish an indexed Google Business Profile and basic online web catalogue.",
        "skills": ["Google Maps SEO", "HTML/CSS", "Digital Catalog"]
    },
    {
        "id": "task-102",
        "title": "Agri-Market Canva Flyer & Content Pack",
        "company": "Kumasi Fresh Produce Ltd",
        "location": "Ashanti / Remote",
        "category": "Marketing",
        "stipend": "GH₵ 350 + Badge",
        "duration": "1 Week",
        "description": "Design 6 social media flyers and captions promoting weekly farm produce deliveries across Kumasi.",
        "skills": ["Canva", "Social Media", "Copywriting"]
    },
    {
        "id": "task-103",
        "title": "Excel Data Cleaning for Logistics Survey",
        "company": "Tamale Transit Logistics",
        "location": "Northern Region / Remote",
        "category": "Admin",
        "stipend": "GH₵ 300 + Verified Badge",
        "duration": "2 Weeks",
        "description": "Organize and clean 350 regional vendor survey rows using Microsoft Excel for regional transportation routing.",
        "skills": ["MS Excel", "Data Entry", "Accuracy"]
    }
]

my_applications = [
    {
        "id": "app-101",
        "projectTitle": "Setup Google Business & Basic Product Catalog",
        "company": "Accra Artisans Collective",
        "dateApplied": "Oct 12, 2026",
        "status": "Under Review"
    }
]

my_badges = [
    {"name": "Digital Readiness Badge", "issuer": "SkillBridge GH", "date": "Sep 2026", "icon": "fa-certificate"},
    {"name": "Web Setup Specialist", "issuer": "Accra Tech Hub", "date": "Aug 2026", "icon": "fa-code"}
]

@app.route("/")
def index():
    return render_template("index.html", opportunities=opportunities, applications=my_applications, badges=my_badges)

@app.route("/api/apply", methods=["POST"])
def apply_task():
    data = request.json
    new_app = {
        "id": f"app-{len(my_applications) + 102}",
        "projectTitle": data.get("title"),
        "company": "Verified SME",
        "dateApplied": "Just Now",
        "status": "Under Review"
    }
    my_applications.insert(0, new_app)
    return jsonify({"success": True, "applications": my_applications})

@app.route("/api/post", methods=["POST"])
def post_task():
    data = request.json
    new_task = {
        "id": f"task-{len(opportunities) + 104}",
        "title": data.get("title"),
        "company": data.get("company"),
        "location": "Ghana / Remote",
        "category": data.get("category"),
        "stipend": data.get("stipend"),
        "duration": data.get("duration"),
        "description": data.get("description"),
        "skills": [data.get("category"), "Micro-Internship"]
    }
    opportunities.insert(0, new_task)
    return jsonify({"success": True, "opportunities": opportunities})

if __name__ == "__main__":
    app.run(debug=True, port=5000)