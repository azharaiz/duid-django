import json


class UtilTarget:
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
