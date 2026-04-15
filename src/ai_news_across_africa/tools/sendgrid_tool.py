from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content


class SendEmailInput(BaseModel):
    """Input schema for SendGridMailTool."""
    to_email: str = Field(..., description="Recipient email address")
    subject: str = Field(..., description="Email subject line")
    html_content: str = Field(..., description="HTML content of the email")
    from_email: str = Field(default="noreply@aiafricabriefing.com", description="Sender email address (optional)")


class SendGridMailTool(BaseTool):
    name: str = "send_email_via_sendgrid"
    description: str = (
        "Send an email using SendGrid. Useful for delivering the AI Africa briefing report "
        "or any other HTML-formatted content via email."
    )
    args_schema: Type[BaseModel] = SendEmailInput

    def _run(self, to_email: str, subject: str, html_content: str, from_email: str = "noreply@aiafricabriefing.com") -> str:
        """
        Send an email via SendGrid API.
        
        Args:
            to_email: Recipient email address
            subject: Email subject
            html_content: HTML content of the email
            from_email: Sender email address
            
        Returns:
            Status message indicating success or failure
        """
        try:
            sendgrid_api_key = os.getenv('SENDGRID_API_KEY')
            
            if not sendgrid_api_key:
                return "Error: SENDGRID_API_KEY environment variable not set"
            
            sg = SendGridAPIClient(sendgrid_api_key)
            
            message = Mail(
                from_email=Email(from_email),
                to_emails=To(to_email),
                subject=subject,
                html_content=Content("text/html", html_content)
            )
            
            response = sg.send(message)
            
            if response.status_code in [200, 201]:
                return f"Email successfully sent to {to_email}"
            else:
                return f"Failed to send email. Status code: {response.status_code}"
                
        except Exception as e:
            return f"Error sending email: {str(e)}"
