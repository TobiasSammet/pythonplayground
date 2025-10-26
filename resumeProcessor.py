import json
from typing import List

class ResumeProcessor:
    def __init__(self, json_data):
        self.data = json.loads(json_data)
        
    
    @classmethod
    def from_file(cls, filename):
        """Create a ResumeProcessor instance from a JSON file"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                json_data = f.read()
                return cls(json_data)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")
            raise
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in file")
            raise
    
    def process_resume_to_text(self, version_type: List[str]) -> str :
        ret_val: str = "<body>"
        contact_info:str = f"<b>{self._get_contact_info_key("name")}</b><br />\n"
        contact_info += f"{self._get_contact_info_key("title", version_type)}<br />\n"
        contact_info += f"{self._get_contact_info_key("address")}<br />\n"
        contact_info += f"{self._get_contact_info_key("phone")}<br />\n"
        contact_info += f"{self._get_contact_info_key("email")}<br />\n"

        professional_summary = f"<br />\n<b>Professional Summary</b><br />\n"
        professional_summary += f"{self.get_professional_summary(version_type)}<br />\n"

        work_experience = f"<br />\n<b>Work Experience<br /></b>\n"
        work_experience += self.get_work_experiences(version_type)
        
        education = ""
        if self.check_root_section_exists_and_has_data('education') :
            education = f"<br /><b>\nEducation</b><br />\n"
            education += self.get_education()
        technical_skills = ""
        if self.check_root_section_exists_and_has_data('technicalSkills') :
            technical_skills = f"<br />\n<b>Technical Expertise</b><br />\n"
            technical_skills += self.get_technical_skills()


        ret_val += f"{contact_info}{professional_summary}{technical_skills}{work_experience}{education}"
        ret_val += "</body>"
        return ret_val
    
    def check_root_section_exists_and_has_data(self, key: str) -> bool :
        if not hasattr(self, 'data'):  # Add safety check
            raise AttributeError("self.data has not been initialized")
        # First, check if 'education' key exists
        if key not in self.data:
            return False
        
        # Then verify it's a non-empty list
        if not isinstance(self.data[key], list) or len(self.data[key]) == 0:
            return False
            
        return True


    def get_work_experiences(self, version_type: List[str]) -> str:
        ret_val: str = ""
        for work_experience in self.data["employmentHistory"]:
            ret_val += f"{work_experience["jobTitle"]}<br />\n"
            ret_val += f"{work_experience["companyName"]}<br />\n"
            ret_val += f"{work_experience["employmentDate"]}<br />\n"
            ret_val += "<ul>"
            for accomplishment in work_experience['accomplishments']:
                if accomplishment["versionType"] == "":
                    ret_val += f"<li>{accomplishment["description"]}</li>\n"
                else:
                    items = set(version_type) & set(accomplishment["versionType"])
                    # Check if version_type is in the list of versions
                    if bool(items):
                        ret_val += f"<li>{accomplishment['description']}</li>\n"
            ret_val += "</ul>\n"
        return ret_val            

    def get_technical_skills(self) -> str:
        ret_val: str = ""
        for techSkills in self.data["technicalSkills"]:
            ret_val += f"{techSkills["title"]}: {techSkills["skills"]}<br />\n"
        return ret_val

    def get_education(self) -> str :
        ret_val: str = ""
        for educationExperience in self.data["education"]:
            ret_val += f"{educationExperience["certificate"]}<br />\n"
            ret_val += f"{educationExperience["school"]}<br />\n"
            if "address" in educationExperience :
                ret_val += f"{educationExperience["address"]}<br />\n<br />\n"
        return ret_val
    
    def get_professional_summary(self, version_type: List[str]) -> str:

        default_summary: str = ""
        matching_summary: str = ""
        # Process professional summaries
        for summary in self.data['professionalSummaries']:
            if summary["versionType"] == "":
                default_summary = summary["summaryText"]
            elif (summary["versionType"] in version_type) and matching_summary == "":
                matching_summary = summary["summaryText"]

        if matching_summary != "":
            return matching_summary
        return default_summary
        

    def _get_contact_info_key(self, key: str, version_type=None, empty_if_not_found: bool = True) -> str:
        if version_type is None:
            version_type = []
        try:
            if len(version_type) == 0:
                return self.data["contactInfo"][key]
            else:
                for version in version_type:
                    if f"{key}-{version}" in self.data["contactInfo"]:
                        return self.data["contactInfo"][f"{key}-{version}"]
                return self.data["contactInfo"][key]
        except:
            if empty_if_not_found:
                return ""
            else:
                return "NOT FOUND"



def main():
    # Process resume from a file
    processor = ResumeProcessor.from_file("c:\\zzz\\resume\\resumeData.json")
    # result = processor.process_resume_to_text(['developer'])
    # result = processor.process_resume_to_text(['backend'])
    # result = processor.process_resume_to_text(['backend', 'developer', 'full-stack'])
    # result = processor.process_resume_to_text(['developer', 'full-stack'])
    # result = processor.process_resume_to_text(['frontend', 'developer'])
    result = processor.process_resume_to_text(['developer', 'full-stack', 'frontend', 'backend', 'mobile'])
    # result = processor.process_resume_to_text(['developer', 'full-stack', 'frontend', 'backend'])
    # result = processor.process_resume_to_text(['developer', 'full-stack', 'frontend', 'backend', 'leadrole', 'mobile'])
    print(result)


if __name__ == "__main__":
    main()