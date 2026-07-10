import api from "./axios";


export const checkoutOrder = async () => {

    const response = await api.post(
        "/orders/checkout"
    );

    return response.data;

};



export const getMyOrders = async () => {

    const response = await api.get(
        "/orders/my"
    );

    return response.data;

};