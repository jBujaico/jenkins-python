pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                git branch: 'main', url: 'https://github.com/jBujaico/jenkins-python.git'
            }
        }

        stage('Ejecutar ETL') {
            steps {
                sh 'python hello.py'
            }
        }
    }
}
