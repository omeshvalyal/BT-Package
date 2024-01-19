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
    stage('Execute Python Script') {
            steps {
                script {
                    sh 'python3 ${workspace}/trigger.py'
                }
            }
        }   
    }
}
