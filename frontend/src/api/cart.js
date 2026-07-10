import api from "./axios";


export const addToCart = async (serviceId) => {

    const response = await api.post(
        "/cart/add",
        {
            service_id: serviceId,
        }
    );

    return response.data;
};


export const getCart = async () => {

    const response = await api.get(
        "/cart/"
    );

    return response.data;
};


export const removeFromCart = async (itemId) => {

    const response = await api.delete(
        `/cart/item/${itemId}`
    );

    return response.data;
};


export const clearCart = async () => {

    const response = await api.delete(
        "/cart/clear"
    );

    return response.data;
};
