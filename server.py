"""connexion file for swagger"""
import connexion

APP = connexion.App(__name__, specification_dir='end_point/')

APP.add_api('swagger.yml')

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=5000, debug=True)
