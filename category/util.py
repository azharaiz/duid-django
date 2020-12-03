import json

class UtilCategory:
    @staticmethod
    def get_jwt_token(client, email, password):
        response_token = client.post(
            '/api/auth/token/',
            {
                'email': email,
                'password': password
            },
            format='json'
        )
        
        jwt_token = json.loads(response_token.content).get('access')
        return jwt_token
    
    @staticmethod
    def get_list_category_title(list_category):
        json_category_title_list = []
        for category_item in list_category:
            json_category_title_list.append(category_item.get("category_title"))
        return json_category_title_list