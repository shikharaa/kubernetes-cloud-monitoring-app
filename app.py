import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    Message = None
    if cpu > 80 or memory > 80 or disk > 40:
        Message = "High CPU or Memory Detected, scale up!!!"
    return render_template("index.html", cpu_metric=cpu, mem_metric=memory, message=Message, disk_metric = disk)

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0') #0.0.0.0 means it is available externally 