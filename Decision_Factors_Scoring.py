import streamlit as st
from fpdf import FPDF


def app():
    st.title("Decision Factors Scoring")
    st.write("Rate the extent to inflence of 27 decision factors for digital twin implementation in the construction projec.You can only assign weight of 1 to 5 to each factor (i.e., 1=Very insignificant, 2=Insignificant, 3=Slightly significant, 4=Significant, and 5=Very significant).Assessment score will be stored in this app.After Completing the form, the final suitability,assessment score will be computed along with a corressponding action plan or recommendations, based on the suitability score.")

    
    factors = {
        'Project Characteristics': ['Complexity of the Project', 'Client Requirements', 'Regulatory Requirements', 'Strict Maintenance Requirements', 'Safety Requirements', 'Data Privacy and Security Requirements', 'Feasibility of Generating Federated Model of Project', 'Availability of funds and affordability of the solution', 'Greenfield vs. Brownfield', 'Size of project'],
        'Location Attributes': ['Remote Location', 'Harsh Weather Conditions', 'Unstable Soil and Ground Conditions', 'Presence of Physically Inaccessible Project Elements'],
        'Industry Readiness': ['Awareness, Knowledge, and Expertise of project actors in DT', 'Organizational Readiness to Adopt DT', 'Availability of Enabling Technologies', 'Availability of High-quality Federated Data', 'Presence of Supportive Regulations'],
        'Project Objectives': ['Real-time Monitoring and Automated Project Control', 'Safety Monitoring', 'Data-Driven Project Planning and Logistics', 'Asset Performance Assessment', 'Smart Design', 'Quality Assessment and Controls', 'Minimal Construction Defects and Reworks', 'Cost of implementation']
    }

    score_mapping = {
        'Complexity of the Project': {1: 1, 2: 2, 3: 2, 4: 3, 5: 4},
        'Client Requirements': {1: 1, 2: 2, 3: 2, 4: 3, 5: 4},
        'Regulatory Requirements': {1: 1, 2: 2, 3: 2, 4: 3, 5: 3},
        'Strict Maintenance Requirements': {1: 1, 2: 2, 3: 2, 4: 3, 5: 4},
        'Safety Requirements': {1: 1, 2: 2, 3: 2, 4: 3, 5: 4},
        'Data Privacy and Security Requirements': {1: 1, 2: 2, 3: 2, 4: 3, 5: 4},
        'Feasibility of Generating Federated Model of Project': {1: 1, 2: 2, 3: 2, 4: 3, 5: 4},
        'Availability of funds and affordability of the solution': {1: 1, 2: 2, 3: 2, 4: 3, 5: 4},
        'Greenfield vs. Brownfield': {1: 1, 2: 2, 3: 2, 4: 3, 5: 4},
        'Size of project': {1: 1, 2: 2, 3: 2, 4: 3, 5: 4},

        'Remote Location': {1: 1, 2: 2, 3: 2, 4: 3, 5: 3},
        'Harsh Weather Conditions': {1: 1, 2: 2, 3: 2, 4: 3, 5: 3}, 
        'Unstable Soil and Ground Conditions': {1: 1, 2: 1, 3: 2, 4: 2, 5: 3}, 
        'Presence of Physically Inaccessible Project Elements': {1: 1, 2: 2, 3: 2, 4: 3, 5: 3},

        'Awareness, Knowledge, and Expertise of project actors in DT': {1: 1, 2: 2, 3: 3, 4: 3, 5: 4}, 
        'Organizational Readiness to Adopt DT': {1: 1, 2: 2, 3: 3, 4: 3, 5: 4},
        'Availability of Enabling Technologies': {1: 1, 2: 2, 3: 3, 4: 3, 5: 4}, 
        'Availability of High-quality Federated Data': {1: 1, 2: 2, 3: 3, 4: 3, 5: 4}, 
        'Presence of Supportive Regulations': {1: 1, 2: 2, 3: 2, 4: 3, 5: 4},

        'Real-time Monitoring and Automated Project Control': {1: 1, 2: 2, 3: 2, 4: 3, 5: 4}, 
        'Safety Monitoring': {1: 1, 2: 2, 3: 2, 4: 3, 5: 4}, 
        'Data-Driven Project Planning and Logistics': {1: 1, 2: 2, 3: 2, 4: 3, 5: 4},
        'Asset Performance Assessment': {1: 1, 2: 2, 3: 2, 4: 3, 5: 4}, 
        'Smart Design': {1: 1, 2: 2, 3: 2, 4: 3, 5: 3},
        'Quality Assessment and Controls': {1: 1, 2: 2, 3: 2, 4: 3, 5: 3}, 
        'Minimal Construction Defects and Reworks': {1: 1, 2: 2, 3: 2, 4: 3, 5: 3}, 
        'Cost of implementation': {1: 1, 2: 2, 3: 2, 4: 3, 5: 4},
    }

    recommendations = {
        "Complexity of the Project": {
            1: "Considering the very low complexity of the project, it may not be necessary to implement a DT.",
            2: "Considering the very low complexity of the project, it may not be necessary to implement a DT.",
            3: "Assess the specific aspects of the project that could benefit from DT technology before applying. These aspects might include simulation and visualization etc."
        },
        "Client Requirements": {
            1: "It is not essential to implement DT as the Client does not require it.",
            2: "It is not essential to implement DT as the Client does not require it.",
            3: "Determine the degree to which the DT complies with project goals and client expectations."
        },
        "Regulatory Requirements": {
            1: "Consider less complicated tools and techniques when regulatory requirements are low",
            2: "Consider less complicated tools and techniques when regulatory requirements are low",
            3: "DT embracement might be beneficial in ensuring compliances."
        },
        "Strict Maintenance Requirements": {
            1: "Ensure to focus on basic maintenance practices and traditional methods to ensure system reliability and performance",
            2: "Ensure to focus on basic maintenance practices and traditional methods to ensure system reliability and performance",
            3: "Assess how the digital twin can help in planning and executing maintenance tasks more effectively"
        },
        "Safety Requirements": {
            1: "Consider using simpler tools and methods to meet safety needs without significant investment in DT",
            2: "Consider using simpler tools and methods to meet safety needs without significant investment in DT",
            3: "Assess how the DT can help in planning and executing safety measures more effectively"
        },
        "Data Privacy and Security Requirements": {
            1: "Focus on basic data protection practices and ensure compliance with minimal security standards using traditional methods",
            2: "Focus on basic data protection practices and ensure compliance with minimal security standards using traditional methods",
            3: "Implement a DT to enhance visibility and control over data privacy and security practices, ensuring that they meet moderate standards"
        },
        "Feasibility of Generating Federated Model of Project": {
            1: "Focus on traditional project management and coordination methods, as the effort and resources required to create a federated model may not be justified given the low feasibility",
            2: "Focus on traditional project management and coordination methods, as the effort and resources required to create a federated model may not be justified given the low feasibility",
            3: "Use the DT for key aspects of the project where the federated model can add significant value"
        },
        "Remote Location": {
            1: "Invest resources on the on-site visit and simpler remote management tools to manage the project effectively ",
            2: "Invest resources on the on-site visit and simpler remote management tools to manage the project effectively ",
            3: "Use the DT to provide better oversight and control, reducing the need for frequent on-site visits and improving efficiency"
        },
        "Harsh Weather Conditions": {
            1: "Commit to use simpler tools can help in planning and mitigating occasional weather disruptions",
            2: "Commit to use simpler tools can help in planning and mitigating occasional weather disruptions",
            3: "Seek advice to use the DT to improve response times and decision-making during adverse weather conditions"
        },
        "Unstable Soil and Ground Conditions": {
            1: "Consider simpler geotechnical monitoring tools if the DT's advantages are minimal",
            2: "Consider simpler geotechnical monitoring tools if the DT's advantages are minimal",
            3: "Arrange site visits and inspections for better understanding the condition of ground before implementing DT"
        },
        "Presence of Physically Inaccessible Project Elements": {
            1: "Focus on standard project management practices without involving DT",
            2: "Focus on standard project management practices without involving DT",
            3: "Assess how the digital twin can help in monitoring, inspecting, and maintaining these elements"
        },
        "Awareness, Knowledge, and Expertise of project actors in DT": {
            1: "Focus on basic training and building foundational knowledge about DT among the team before introducing DT",
            2: "Focus on basic training and building foundational knowledge about DT among the team before introducing DT",
            3: "Conduct comprehensive training sessions to enhance the team's skills and confidence in using DT"
        },
        "Organizational Readiness to Adopt DT": {
            1: "Invest in preliminary steps to improve organizational readiness, such as training key stakeholders, establishing a digital transformation strategy, and securing leadership buy-in",
            2: "Invest in preliminary steps to improve organizational readiness, such as training key stakeholders, establishing a digital transformation strategy, and securing leadership buy-in",
            3: "Develop a clear implementation roadmap, provide targeted training, and ensure adequate resources and identify gaps that need to be addressed "
        },
        "Availability of Enabling Technologies": {
            1: "Identify the specific technologies that are lacking and create a plan to acquire and integrate these technologies incrementally",
            2: "Identify the specific technologies that are lacking and create a plan to acquire and integrate these technologies incrementally",
            3: "Commit to develop a comprehensive plan to enhance technology availability, including investing in IoT devices, data analytics tools, and robust connectivity solutions"
        },
        "Availability of High-quality Federated Data": {
            1: "Develop a phased plan to enhance data collection, management practice and work on improving data quality and integration",
            2: "Develop a phased plan to enhance data collection, management practice and work on improving data quality and integration",
            3: " Invest in improving data quality, standardizing data formats, and integrating disparate data sources"
        },
        "Presence of Supportive Regulations": {
            1: "Assess the specific regulatory obstacles and develop strategies to navigate them",
            2: "Assess the specific regulatory obstacles and develop strategies to navigate them",
            3: "Work with legal and regulatory experts to ensure compliance and address any ambiguities in DT adoption"
        },
        "Real-time Monitoring and Automated Project Control": {
            1: "Focus on traditional project management methods and manual controls to oversee project activities",
            2: "Focus on traditional project management methods and manual controls to oversee project activities",
            3: "Identify key project activities where real-time insights and automation can improve efficiency and decision-making"
        },
        "Safety Monitoring": {
            1: "Use manual monitoring or other low key safety management methods to ensure project safety",
            2: "Use manual monitoring or other low key safety management methods to ensure project safety",
            3: "Identify key safety-critical activities where real-time monitoring and analytics can improve safety outcomes before implementing DT"
        },
        "Data-Driven Project Planning and Logistics": {
            1: "Consider manual logistics management or starting with simpler digital tools to enhance planning and logistics",
            2: "Consider manual logistics management or starting with simpler digital tools to enhance planning and logistics",
            3: "Evaluate whether specific aspects of the project could benefit from data-driven insights and optimization"
        },
        "Asset Performance Assessment": {
            1: "Ensure periodic inspections and manual performance evaluations without DT adoption",
            2: "Ensure periodic inspections and manual performance evaluations without DT adoption",
            3: "Commit to integrate the DT with critical assets or systems where real-time monitoring and predictive analytics can enhance performance assessment"
        },
        "Smart Design": {
            1: "Prioritize conventional design methodologies and collaborative planning processes",
            2: "Prioritize conventional design methodologies and collaborative planning processes",
            3: "Ensure the implementation of DT into critical design phases where real-time simulations and virtual prototyping can optimize design iterations and mitigate risks"
        },
        "Quality Assessment and Controls": {
            1: "Ensure consistent manual inspections and periodic audits to improve decision making",
            2: "Ensure consistent manual inspections and periodic audits to improve decision making",
            3: "Concentrate on incorporating DT into key quality assurance processes, such as defect detection, root cause analysis, and performance monitoring before immediate implementation"
        },
        "Minimal Construction Defects and Reworks": {
            1: "Arrange frequent onsite supervisions and manual inspections to reduce construction defects and reworks",
            2: "Arrange frequent onsite supervisions and manual inspections to reduce construction defects and reworks",
            3: "Use DT for real-time quality monitoring and defect detection but start with critical components and expand as benefits are realized"
        },
        "Availability of funds and affordability of the solution": {
            1: "Explore grants, subsidies, or partnerships that could provide additional funding otherwise improve efficiency with low cost",
            2: "Explore grants, subsidies, or partnerships that could provide additional funding otherwise improve efficiency with low cost",
            3: "Look for advanced features and capabilities that can drive innovation and significantly enhance project outcomes."
        },
        "Greenfield vs. Brownfield": {
            1: "Focus on basic project management tools and traditional methods suited for either Greenfield (new construction) or Brownfield (modifying existing structures) environments.",
            2: "Focus on basic project management tools and traditional methods suited for either Greenfield (new construction) or Brownfield (modifying existing structures) environments.",
            3: "For Greenfield projects, use digital twins to enhance design accuracy, streamline construction processes, and simulate different scenarios. For Brownfield projects, leverage digital twins for detailed analysis of existing conditions, clash detection, and efficient integration of new elements"
        },
        "Size of project": {
            1: "Consider using basic digital solutions for specific tasks and reassess the need for a comprehensive digital twin as the project scope or complexity increases",
            2: "Consider using basic digital solutions for specific tasks and reassess the need for a comprehensive digital twin as the project scope or complexity increases",
            3: "Focus on key project phases where a DT can provide the most value, such as design optimization, construction planning, and quality control."
        },
        "Cost of implementation": {
            1: "Prioritize low-cost or free digital tools to manage the project",
            2: "Prioritize low-cost or free digital tools to manage the project",
            3: "Prioritize features that provide the most value and ensure that the DT aligns with the project’s overall budget constraints"
        },
    }

    if 'scores' not in st.session_state:
        st.session_state.scores = {factor: 1 for group in factors.values() for factor in group}

    total_score = 0  # Initialize total_score to 0 for each run

    for group, group_factors in factors.items():
        st.subheader(group)
        for factor in group_factors:
            st.session_state.scores[factor] = st.selectbox(factor, list(range(1, 6)), index=st.session_state.scores[factor]-1)
            total_score += score_mapping[factor][st.session_state.scores[factor]]  # Accumulate score based on factor and score

    if st.button("Total Score"):
        st.write(f"Total Score: {total_score}")

    if st.button("Check Suitability"):
        if total_score < 50:
            st.write("Suitability: Low")
        elif 50 <= total_score < 60:
            st.write("Suitability: Average")
        elif 61 <= total_score < 80:
            st.write("Suitability: Medium")    
        else:
            st.write("Suitability: High")

    if st.button("Generate Recommendations"):
        st.write("Recommendations:")
        for factor, score in st.session_state.scores.items():
            if score <= 3:  # Only generate recommendations for scores 1, 2, and 3
                st.write(f"{factor}: {recommendations[factor][score]}")

    if st.button("Print Preview"):
        st.write("Project Details:")
        st.write(f"Name of User: {st.session_state.project_details['name_of_user']}")
        st.write(f"Name of Project: {st.session_state.project_details['name_of_project']}")
        st.write(f"Assessment Date: {st.session_state.project_details['assessment_date']}")
        st.write(f"Type of Project: {st.session_state.project_details['type_of_project']}")
        st.write(f"Total Score: {total_score}")
        if total_score < 40:
            st.write("Suitability: Low")
        elif 40 <= total_score < 60:
            st.write("Suitability: Medium")
        else:
            st.write("Suitability: High")
        st.write("Recommendations:")
        for factor, score in st.session_state.scores.items():
            if score <= 3:  # Only generate recommendations for scores 1, 2, and 3
                st.write(f"{factor}: {recommendations[factor][score]}")


    if st.button("Download Report"):
        pdf = FPDF()
        pdf.add_page()
        # Set title font (bold, larger size)
        pdf.set_font("Arial", style='B', size=16)

# Get the width of the title and calculate the center position
        title = "DT implementation Report"
        title_width = pdf.get_string_width(title)
        
        horizontal_position = (210 - title_width) / 2 + 8  # 210 is the page width of A4, adjust with your desired position

# Set the X position explicitly and add the title
        pdf.set_x(horizontal_position)
        pdf.cell(title_width, 10, title, ln=True, align='C')
# Add space after the title
        pdf.ln(10)



        pdf.set_font("Arial", size=10)
        
        # Add Project Detail
        if 'project_details' in st.session_state:
            project_details = st.session_state.project_details
            pdf.set_font("Arial", style='B', size=10)
            pdf.cell(200, 10, txt="Project Details", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Name of User: {project_details['name_of_user']}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Name of Project: {project_details['name_of_project']}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Assessment Date: {project_details['assessment_date']}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Type of Project: {project_details['type_of_project']}", ln=True, align='L')
            
        if 'scores' in st.session_state:
            scores = st.session_state.scores
            total_score = sum(scores.values())
            
            pdf.cell(200, 10, txt=f"Total Score: {total_score}", ln=True, align='L')
            
        if total_score < 40:
                suitability = "Low"
        elif 40 <= total_score < 60:
                suitability = "Medium"
        else:
                suitability = "High"
            
            # Add Suitability to PDF
        pdf.cell(200, 10, txt=f"Suitability: {suitability}", ln=True, align='L')
        pdf.ln(5)  # Adding space before the next section
        pdf.set_font("Arial", style='B', size=10)
        pdf.cell(200, 10, txt="Recommendations:", ln=True, align='L')
        for factor, score in st.session_state.scores.items():
            if score <= 3:
                pdf.set_font("Arial", style='B', size=10)
                pdf.cell(200, 8, txt=f"{factor}:", ln=True, align='L')
                pdf.set_font("Arial", style='', size=10)
                pdf.multi_cell(200, 8, txt=f"{recommendations[factor][score]}", align='L') 

        pdf_file = "decision_factors_report.pdf"
        pdf.output(pdf_file)
     
        
        st.download_button(label="Download ", data=open(pdf_file, "rb").read(), file_name=pdf_file)         

    
          
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Back"):
            st.session_state.page = 'Project Parameters'
            st.rerun()

if __name__ == '__main__':
    app()
