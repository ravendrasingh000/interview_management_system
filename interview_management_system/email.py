import frappe
from frappe.utils import get_url

def send_email_for_apply(doc, method):

    message = f"""
    Dear { doc.full_name },<br><br>
    Thank you for applying for the {doc.job_applied_for} position.<br>
    Our HR team will contact you shortly if your profile matches our requirements...<br>
    Best regards,<br>
    HR Team
    """

    # Send email
    frappe.sendmail(
        recipients=[doc.email],
        subject="Thank You for Applying",
        message=message
    )


# ................................................................................................


def handle_status_based(doc, method):


    candidate_doc = frappe.get_doc("Candidate", doc.candidate)
    candidate_name = candidate_doc.full_name

    job_doc = frappe.get_doc("Job Opening", doc.job_position)
    job_title = job_doc.job_title

    interviewer_doc = frappe.get_doc("Interviewer", doc.interviewer_name)
    itrvier_name = interviewer_doc.name1



    if doc.status == "Scheduled":
        frappe.sendmail(
            recipients=[doc.email],
            subject="Interview Scheduled",
                message = f"""
                Dear {candidate_name},<br><br>
                Congratulations!<br>
                You have been shortlisted for interview round for the {job_title} position.<br>
                Your interview is scheduled on {doc.interview_date} at {doc.time}.<br>
                Interviewer Name: {itrvier_name}<br>
                Location/Mode: {doc.mode}<br>
                Meeting Link: {doc.meeting_link}<br>
                Please be available on time.<br>
                Best regards,<br>
                HR Team
                """
        )

    elif doc.status == "Conducted":
        frappe.sendmail(
            recipients=[doc.email],
            subject="Interview Completed",
            message = f"""
                Dear {candidate_name},<br><br>
                Thank you for attending the interview for the {job_title} position on {doc.interview_date}.<br>
                We appreciate your time and interest in joining our team.<br>
                Our recruitment team will now evaluate your interview and get back to you shortly with the next steps.<br>
                Best regards,<br>
                HR Team
                """
        )

    elif doc.status == "Rejected":
        frappe.sendmail(
            recipients=[doc.email],
            subject="Interview Result - Not Selected",
            message = f"""
                Dear {candidate_name},<br><br>
                Thank you for taking the time to attend the interview for the {job_title} position.<br>
                After careful evaluation, we regret to inform you that you have not been selected for this role at this time.<br><br>
                We appreciate your interest in our company and encourage you to apply for future openings that match your profile.<br><br>
                Wishing you all the best in your career journey.<br><br>
                Best regards,<br>
                HR Team
                """
        )


    elif doc.status == "Approved":
        frappe.sendmail(
            recipients=[doc.email],
            subject="Interview Result - Selected",
            message = f"""
                Dear {candidate_name},<br><br>
                Congratulations!<br>
                We are pleased to inform you that you have successfully cleared the interview round for the position of {job_title}.<br>
                Our HR team will contact you shortly with the next steps regarding the offer letter and joining formalities.<br><br>
                We look forward to welcoming you onboard.<br><br>
                Best regards,<br>
                HR Team
                """
        )
        

    
