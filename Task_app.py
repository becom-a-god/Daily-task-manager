from flask import Flask, render_template, request, redirect, url_for
from  datetime import date
from task_db import create_tables, save_task, get_task, search_task, delete_task, change_status, completed_task
create_tables()

task_app = Flask(__name__)

@task_app.route("/", methods=["POST","GET"])
def home_page():
    if request.method == "POST":
        search_data = request.form.get("search-bar")
        task_id = request.form.get("delete")
        yes_id = request.form.get("yes")
        status = request.form.get("status")
        if search_data:
            return render_template("index.html",tasks=search_task(search_data),total_task=len(get_task()),completed_task=len(completed_task()))
        if task_id:
             return render_template("index.html",confirm_delete=True,tasks=get_task(),delete_id=task_id,total_task=len(get_task()),completed_task=len(completed_task()))
        if yes_id:
             delete_task(yes_id)
        if status:
             change_status(status)
    return render_template("index.html",tasks=get_task(),total_task=len(get_task()),completed_task=len(completed_task()))

@task_app.route("/create_task", methods=["POST","GET"])
def create_task():
    if request.method == "POST":
        title = request.form.get("title")
        task = request.form.get("task")
        today_date = str(date.today())
        save_task(title,task,False,today_date)
        return redirect(url_for('home_page'))
    return render_template("create_task.html")

task_app.run(debug=False, port=5000)
