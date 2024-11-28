import json
import os
from company_data_extraction.crew import CompanyDataExtraction

def gather_company_info(company_name):
    inputs = {
        'company_name': company_name
    }

    crew_output = CompanyDataExtraction().crew().kickoff(inputs=inputs)

    output_file = "company_data.json"

    if os.path.exists(output_file):
        with open(output_file, "r") as file:
            json_data = json.load(file)
        return json_data
    else:
        raise FileNotFoundError(f"Expected JSON file '{output_file}' not found.")


def run():
    """
    Run the crew.
    """
    inputs = {
        'company_name': 'Avid Accountants Ltd'
    }
    CompanyDataExtraction().crew().kickoff(inputs=inputs)
