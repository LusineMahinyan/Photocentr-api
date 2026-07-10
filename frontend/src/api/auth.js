import api from "./axios";

export const registerUser = async (userData) => {
    const response = await api.post(
        "/users/register",
        userData
    );

    return response.data;
};

export const loginUser = async (email, password) => {

    const formData = new URLSearchParams();

    formData.append("username", email);
    formData.append("password", password);

    const response = await api.post(
        "/users/login",
        formData,
        {
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
        }
    );

    localStorage.setItem(
        "access_token",
        response.data.access_token
    );

    return response.data;
};
