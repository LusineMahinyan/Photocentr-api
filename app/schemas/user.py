from pydantic import BaseModel, ConfigDict, EmailStr,ValidationInfo, field_validator
import re


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    password: str
    confirm_password: str

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v):
        if not re.fullmatch(r"^\+7\d{10}$", v):
            raise ValueError("Phone must start with +7 and contain 10 digits")
        return v

    @field_validator("password")
    @classmethod
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")

        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain 1 uppercase letter")

        if not re.search(r"[$%&!:]", v):
            raise ValueError("Password must contain 1 special character ($%&!:)")

        if not re.fullmatch(r"[A-Za-z0-9$%&!:]+", v):
            raise ValueError("Password must contain only Latin letters")

        return v

    @field_validator("confirm_password")
    @classmethod
    def passwords_match(cls, v: str, info: ValidationInfo):
        if v != info.data.get("password"):
            raise ValueError("Passwords do not match")
        return v


class UserOut(BaseModel):
    id: int
    full_name: str
    email: str
    phone: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)