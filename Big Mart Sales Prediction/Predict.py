import pickle


def model_prediction(features):
    pickled_model = pickle.load(open('Big_Mart_Sale_lasso.pkl', 'rb'))
    Item_Outlet_Sales = str(list(pickled_model.predict(features)))

    return str(f'The Sales is {Item_Outlet_Sales}')


Item_Weight = int(input())

Item_Visibility = int(input())
Item_MRP = int(input())

Outlet_Identifier = int(input())

Outlet_Years = int(input())

Item_Fat_Content_0 = int(input())
Item_Fat_Content_1 = int(input())
Item_Fat_Content_2 = int(input())

Outlet_Size_0 = int(input())
Outlet_Size_1 = int(input())
Outlet_Size_2 = int(input())

Outlet_Location_Type_0 = int(input())
Outlet_Location_Type_1 = int(input())
Outlet_Location_Type_2 = int(input())

Outlet_Type_0 = int(input())
Outlet_Type_1 = int(input())
Outlet_Type_2 = int(input())
Outlet_Type_3 = int(input())

New_Item_Type_0 = int(input())
New_Item_Type_1 = int(input())



print(model_prediction([[Item_Weight,
            Item_Visibility,
            Item_MRP,
            Outlet_Years,
            Outlet_Identifier,
            Item_Fat_Content_0, Item_Fat_Content_1, Item_Fat_Content_2,
            Outlet_Size_0, Outlet_Size_1, Outlet_Size_2,
            Outlet_Location_Type_0, Outlet_Location_Type_1, Outlet_Location_Type_2,
            Outlet_Type_0, Outlet_Type_1, Outlet_Type_2, Outlet_Type_3,
            New_Item_Type_0, New_Item_Type_1]]))
