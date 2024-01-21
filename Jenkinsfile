pipeline {
    agent any
    environment {
        SSH_AGENT_CREDENTIALS = credentials('remote-host')
        }
    stages {
        stage('Checkout') {
            steps {
                script {
                  git branch: 'main', credentialsId: 'Github', url: 'git@github.com:omeshvalyal/BT-Package.git'
                }
            }
        }
/*
    stage('Connecting to remote server') {
            steps {
                script {
                    sshagent(['remote-host']) {
                    sh "python3 ${workspace}/trigger.py"
                    }
                }
            }
        }
*/
stage('Install Paramiko') {
            steps {
                script {
                    // Install the paramiko module
                    sh 'python3 -m pip install paramiko'
                    sh 'python3 -m pip install mysql-connector-python'
                }
            }
        }
    stage('Execute Python Script') {
            steps {
                script {
                    sh "python3 ${workspace}/trigger3.py"
                }
            }
        }   
    }
}
