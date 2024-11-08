def convert_dict_to_markdown(data):
    """
    Convert the given dictionary into a Markdown-formatted string.
    
    :param data: Dictionary containing the structured information.
    :return: A Markdown-formatted string.
    """
    markdown_content = []

    # Add Title
    markdown_content.append("# Immigration Profile Report\n")
    
    # Add Questionnaire and Response
    markdown_content.append("## 1. Questionnaire and Response:\n")
    questionnaire = data.get('questionnaire', '')
    for line in questionnaire.split('●'):
        if line.strip():  # Avoid empty lines
            markdown_content.append(f"- {line.strip()}\n")
    
    # Add Job Roles
    markdown_content.append("## 2. Job Roles Based on Education and Work Experience:\n")
    markdown_content.append(f"{data.get('job_roles', '')}\n")
    
    # Add NOC Codes
    markdown_content.append("## 3. NOC Codes:\n")
    for noc in data.get('noc_codes', []):
        markdown_content.append(f"- {noc.strip()}\n")
    
    # Add CRS Score Breakdown
    markdown_content.append("## 4. CRS Score Breakdown:\n")
    markdown_content.append(f"{data.get('crs_score', '')}\n")
    
    # Add Roadmap
    markdown_content.append("## 5. Roadmap for Canada Immigration:\n")
    markdown_content.append(f"{data.get('roadmap', '')}\n")
    
    # Combine all the sections into a single string
    return "\n".join(markdown_content)

# Example Data (as per the data you provided)
data = {
    "questionnaire": "Questionnaire and Response: ● Name: Udegbunam Onyinye Ogochukwu ● Date of Birth: 5th May 1995 ● Marital Status: Single ● Will your spouse accompany you? No ● Product Type: EEP/PNP ● IELTS scores for Principal applicant: Listening- 8.5, Reading- 8.0, Speaking- 7.5, and Writing- 7.0 Projected IELTS ● IELTS scores for Dependent spouse: Listening -, Reading -, Speaking -, and Writing - ● Available degrees for Principal applicant: Secondary school certificate and/or OND (Ordinary National Diploma) HND (Higher National Diploma), Bachelor's degree, Post graduate Diploma, Masters degree, PhD (Doctorate): Masters Degree ● Available degrees for Dependent spouse: Secondary school certificate and/or OND (Ordinary National Diploma) HND (Higher National Diploma), Bachelor's degree, Post graduate Diploma, Masters degree, PhD (Doctorate): ● Years of work experience for Principal applicant: 7 years ● Are you self-employed? No ● Have you had a previous Canada visa application? If yes, how many?: None ● Details of Previous Canada visa application: (date/month/year, start and end date the academic qualification that was filled, start and end dates of all work experience filled): None ● Do you have family members who reside in Canada as permanent residents? If yes, specify your relationship with them and the province in which they reside: None ● Do you currently reside in Nigeria? If No, specify the country you currently reside and the date (Date/Month/Year) you left Nigeria: Yes.",
    "job_roles": "Based on the educational background of having a Master's Degree and 7 years of work experience, the most relevant job roles for Udegbunam Onyinye Ogochukwu could be: \n1. Project Manager\n2. Business Analyst\n3. Operations Manager\n4. Human Resources Manager\n5. Marketing Manager\n\nThese roles typically require a higher level of education and work experience, which align with Udegbunam's qualifications.",
    "noc_codes": [
        "NOC 2021 V1.0 Code: 10029\nNOC 2021 V1.0 Title: Other business services managers",
        "NOC 2021 V1.0 Code: 10022\nNOC 2021 V1.0 Title: Advertising, marketing and public relations managers",
        "NOC 2021 V1.0 Code: 11201\nNOC 2021 V1.0 Title: Professional occupations in business management consulting",
        "NOC 2021 V1.0 Code: 10011\nNOC 2021 V1.0 Title: Human resources managers"
    ],
    "crs_score": "Total CRS Score: 468\n\nReasoning:\n1. Age: 25 points\n2. Level of Education: Masters Degree - 135 points\n3. Official Language Proficiency: Listening- 8.5 (29 points), Reading- 8.0 (29 points), Speaking- 7.5 (26 points), Writing- 7.0 (23 points) - Total: 107 points\n4. Work Experience: 7 years - 50 points\n5. Adaptability: No information provided - Assuming 10 points\n6. Additional Factors: No previous Canada visa application, No family members in Canada, Not self-employed - 0 points\n\nTotal CRS Score: 25 + 135 + 107 + 50 + 10 + 0 = 327\n\nAdditional points may be awarded for factors such as provincial nomination, job offer, or French language proficiency, which are not provided in the questionnaire. The total CRS score may vary based on these additional factors.",
    "roadmap": "**ROADMAP**:\n\n**1. Client Information**\n   - Name: [Client's Name]\n   - Age: [Client's Age]\n   - Marital Status: [Client's Marital Status]\n   - Product Type: [Client's Product Type]\n   - Current PA IELTS Scores: [Client's PA IELTS Scores]\n   - Current Spouse IELTS Scores: [Client's Spouse IELTS Scores]\n   - Available Education: [Client's Education]\n   - Years of Work Experience: [Client's Work Experience]\n   - Previous Canada application: [Client's Previous Application Info]\n   - Additional Information: [Client's Additional Information]\n   - Projected CRS score: [Client's Projected CRS Score]\n   - Current CRS score: 327\n\n**2. Projected IELTS Score**\n   - Listening:8.5\n   - Reading:8\n   - Writing:7.5\n   - Speaking:7.5\n\n**3. Required Minimum IELTS Scores**\n   - Listening:7\n   - Speaking:7\n   - Reading:7\n   - Writing:7\n\n**4. Recommended Pathways**\n   1. Federal Skilled Worker - Express Entry Pathway\n   2. Provincial Nomination Pathway\n\n**5. Recommended NOC**\n   - Option A: 10029 - Other business services managers\n   - Option B: 10022 - Advertising, marketing and public relations managers\n   - Option C: 11201 - Professional occupations in business management consulting\n\n**6. Additional Information**\n   - Based on your education and work experience, you might want to consider achieving a higher degree to raise your CRS score.\n\n**7. Timeline with Milestones:**\n   • Eligibility Requirements Completion (Month): 2\n   • Pre-ITA Stage (Month): 3\n   • ITA and Documentation (Month): 5\n   • Biometric Request (Month): 6\n   • Passport Request (PPR) (Month): 11\n   • Confirmation of Permanent Residency (COPR) (Month): 12\n\n**Disclaimer**: These are projected timelines and may vary depending on the turnaround time of each process involved. Please note that while we aim to provide accurate and timely information, we cannot control processing times as they can vary."
}

# Convert the dictionary to Markdown string
markdown_string = convert_dict_to_markdown(data)

# Print the result or use it as input to markdown_pdf
print(markdown_string)
