pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                git 'https://github.com/jBujaico/jenkins-python.git'
            }
        }

        stage('Ejecutar ETL') {
            steps {
                sh 'python hello.py'
            }
        }
    }
}
