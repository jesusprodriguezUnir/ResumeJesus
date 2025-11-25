from dataclasses import dataclass, field
from typing import Any, Dict, Optional
import streamlit as st

@dataclass
class AppState:
    """Type-safe definition of the application state."""
    user_id: Optional[str] = None
    selected_page: str = "resume"
    filters: Dict[str, Any] = field(default_factory=dict)
    # Add more state variables here as needed

class StateManager:
    """Singleton class to manage Streamlit Session State."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StateManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if 'app_state' not in st.session_state:
            st.session_state.app_state = AppState()

    @property
    def state(self) -> AppState:
        """Access the typed application state."""
        return st.session_state.app_state

    def set_page(self, page_name: str):
        """Update the selected page."""
        self.state.selected_page = page_name

    def update_filter(self, key: str, value: Any):
        """Update a specific filter."""
        self.state.filters[key] = value

    def get_filter(self, key: str, default: Any = None) -> Any:
        """Get a filter value."""
        return self.state.filters.get(key, default)
