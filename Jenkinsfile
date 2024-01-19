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
    stage('Connecting to remote server') {
            steps {
                script {
                    sshagent(['remote-host']) {
                    sh "ssh-keyscan -t ed25519 54.91.98.173 >> ~/.ssh/known_hosts"
                    sh "python3 ${workspace}/trigger.py"
                    }
                }
            }
        }
/*    stage('Execute Python Script') {
            steps {
                script {
                    sh "python3 ${workspace}/trigger.py"
                }
            }
        }   
*/
    }
}
