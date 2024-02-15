pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'py --version'
      }
    }
    stage('hello') {
      steps {
        sh 'py hello.py'
      }
    }
  }
}
