# generate_report.py
import subprocess

# Install the necessary dependencies
subprocess.run(['pip', 'install', 'cml-publish'])

# Generate the report.md file
with open('report.md', 'w') as report:
    report.write("## Model Metrics\n")
    with open('metrics.txt') as metrics:
        report.write(metrics.read())

    report.write("\n## Data Viz\n")
    subprocess.run(['cml-publish', 'feature_importance.png', '--md'], stdout=report)
    subprocess.run(['cml-publish', 'residual.png', '--md'], stdout=report)
