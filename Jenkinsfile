pipeline {
    agent none
    stages {
        stage('Build') {
            steps {
                sh 'python sources/stackrox-api-demo.py'
            }
        }
    }
}
