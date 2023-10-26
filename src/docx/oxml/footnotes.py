from docx.oxml.parser import OxmlElement
from docx.oxml.simpletypes import ST_DecimalNumber
from docx.oxml.xmlchemy import BaseOxmlElement, RequiredAttribute


class CT_FNR(BaseOxmlElement):
    _id = RequiredAttribute("w:id", ST_DecimalNumber)

    @classmethod
    def new(cls, _id: int):
        footnoteReference = OxmlElement("w:footnoteReference")
        footnoteReference._id = _id
        return footnoteReference
