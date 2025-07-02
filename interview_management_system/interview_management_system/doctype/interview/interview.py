# Copyright (c) 2025, Ravin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Interview(Document):
    pass
	# def before_save(self):
	# 	if self.candidate:
	# 		# Get the Candidate document by name
	# 		candidate_doc = frappe.get_doc("Candidate", self.candidate)
			
	# 		# Set the job_position from Candidate's job_applied_for
	# 		self.job_position = candidate_doc.job_applied_for
			
	# 		print("Job Title:", candidate_doc.job_applied_for)
