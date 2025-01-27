# Copyright (c) 2024, Cumulations and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Milestones(Document):
	pass
	#def after_insert(self):
	#	category_list = ["Cognitive"]
#
#		for title in category_list:
#			try:
#				new_doc = frappe.new_doc('Category')
#				new_doc.title = "Cognitive"
#				new_doc.milestone = self.name  # Use 'self.name' to refer to the current milestone
#				new_doc.insert()
#			except Exception as e:
#		                # Log the error if category creation fails
#		                frappe.errprint(f"Error creating category {title}: {str(e)}")
