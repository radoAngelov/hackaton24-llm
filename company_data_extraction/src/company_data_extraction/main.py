from company_data_extraction.crew import CompanyDataExtraction

def gather_company_info(company_name):
    inputs = {
        'company_name': company_name
    }
    return CompanyDataExtraction().crew().kickoff(inputs=inputs)

def run():
    """
    Run the crew.
    """
    inputs = {
        'company_name': 'Avid Accountants Ltd'
    }
    CompanyDataExtraction().crew().kickoff(inputs=inputs)
