pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                  git branch: 'main', credentialsId: 'Github', url: 'git@github.com:omeshvalyal/BT-Package.git'
                }
            }
        }
    }
}
