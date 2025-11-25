from pydantic import BaseModel
import os
from typing import Optional

class AppConfig(BaseModel):
    """Application Configuration Settings."""
    APP_NAME: str = "ResumeJesus Enterprise"
    VERSION: str = "2.0.0"
    DEBUG: bool = False
    
    # Contact Info
    EMAIL: str = "jesusprodriguez@gmail.com"
    PHONE: str = "+34 670 402 450"
    LOCATION: str = "Madrid, España"
    
    # External URLs
    LINKEDIN_URL: str = "https://www.linkedin.com/in/jes%C3%BAs-pedro-rodr%C3%ADguez-castro-b746394a/"
    GITHUB_URL: str = "https://github.com/jesusprodriguez"
    BLOG_URL: str = "https://blogpersonal-eta.vercel.app/"
    BLOG_FEED_URL: str = "https://blogpersonal-eta.vercel.app/feed.xml"

    # Theme
    PRIMARY_COLOR: str = "#2563eb"
    
    class Config:
        env_prefix = "APP_"

# Global Config Instance
config = AppConfig()
