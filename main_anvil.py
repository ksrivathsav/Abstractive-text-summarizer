from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    summ=anvil.server.call('input_text',self.text_box_1.text)
    if 1:
      self.reference.visible=True
      self.ref_area.visible=True
      self.eval_button.visible=True
      self.sum.text=summ
  def eval_button_click(self,**event_args):
    r_score=anvil.server.call('eval',self.ref_area.text,self.sum.text)
    if 1:
      self.eval_score.visible=True
      self.eval_score.text=r_score
      self.reference.visible=False
      self.ref_area.visible=False
      self.eval_button.visible=False

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

