pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout source code from a Git repository
                script {
                   git credentialsId: 'githubcredential', url: 'git@github.com:omeshvalyal/BT-Package.git'
}
            }
        }

        // Add more stages for build, test, deploy, etc.
    }

    post {
        success {
            echo 'Pipeline successfully executed!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
