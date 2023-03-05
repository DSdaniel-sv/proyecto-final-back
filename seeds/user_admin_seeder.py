from flask_seeder import Seeder
from app.models.users_model import UserModel


class UserAdminSeeder(Seeder):
    def run(self):
        users = [
            {
                'name': 'daniel',
                'last_name': 'silva',
                'username': 'admin',
                'password': '123456',
                'email': 'administrador@gmail.com',
                'rol_id': 1
            }
        ]
        for user in users:
            record = UserModel.where(username=user['username']).first()
            if not record:
                print(f'Se crea usuario: {user}')
                new_record = UserModel.create(**user)
                new_record.hashPassword()
                self.db.session.add(new_record)
