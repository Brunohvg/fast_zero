from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_create_user(client):
    user_data = {
        'username': 'bruno',
        'email': 'brunovidal27.19@gmail.com',
        'password': '1234567w8',
    }
    response = client.post('/users/', json=user_data)  # Act

    assert response.status_code == HTTPStatus.CREATED  # Assert
    assert response.json() == {
        'username': 'bruno',
        'email': 'brunovidal27.19@gmail.com',
        'id': 1,
    }  # Assert


def test_read_users(client):
    response = client.get('/users/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'users': [
            {
                'username': 'bruno',
                'email': 'brunovidal27.19@gmail.com',
                'id': 1,
            }
        ]
    }  # Assert


def test_update_user(client):
    user_data = {
        'username': 'bruno',
        'email': 'brunovidal27.19@gmail.com',
        'password': '1234567w8',
        'id': 1,
    }
    response = client.put('/users/1', json=user_data)  # Act
    assert response.status_code == HTTPStatus.OK  # Assert
    if response.status_code == HTTPStatus.NOT_FOUND:
        assert response.json() == {'detail': 'User not found'}  # Assert

    assert response.json() == {
        'username': 'bruno',
        'email': 'brunovidal27.19@gmail.com',
        'id': 1,
    }  # Assert


def test_delete_user(client):
    response = client.delete('/users/1')  # Act
    if response.status_code == HTTPStatus.NOT_FOUND:
        assert response.json() == {'detail': 'User not found'}  # Assert

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'User deleted'}  # Assert


def test_read_user(client):
    response = client.get('/users/1')  # Act
    if response.status_code == HTTPStatus.NOT_FOUND:
        assert response.json() == {'detail': 'User not found'}  # Assert

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'username': 'bruno',
        'email': 'brunovidal27.19@gmail.com',
        'id': 1,
    }  # Assert
