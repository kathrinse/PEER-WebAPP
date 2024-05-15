import streamlit as st
from .sidebar import render_sidebar


class BasePage:
    def __init__(self, *, name: str):
        self.__widgets__ = []
        self.__key__ = name

    def sidebar(self):
        render_sidebar()

    def __post_process__(self, session):
        if self.__key__ not in st.session_state.page_widgets.keys():
            st.session_state.page_widgets[self.__key__] = self

    def clear(self):
        for i in self.__widgets__:
            i.empty()

    def append(self, *, empty):
        self.__widgets__.append(empty)

    def extend(self, *, li: list):
        for i in li:
            self.append(empty=i)

    def __getitem__(self, idx):
        return self.__widgets__[idx]

    def __str__(self):
        ret = f'There are {len(self.__widgets__)} widgets:\n'
        for id, article in enumerate(self.__widgets__):
            ret += f'{id + 1}) '
            ret += f'{article}'

        return ret

    # return an iterator that can be used in for loop etc.
    def __iter__(self):
        return self.__widgets__.__iter__()

    def __len__(self):
        return len(self.__widgets__)
