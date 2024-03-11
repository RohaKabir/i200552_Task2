pipeline {
    agent {
        label 'windows'
    }
    stages {
        stage('Checkout repository') {
            steps {
                script {
                    // Checkout repository
                    git branch: 'main', url: 'https://github.com/RohaKabir/i200552_Task2.git'
                }
            }
        }
        stage('Set up Python environment') {
            steps {
                script {
                    // Set up Python environment
                    bat 'python -m venv venv' // On Windows
                    bat 'venv\\Scripts\\activate' // On Windows
                }
            }
        }
        stage('Install dependencies') {
            steps {
                script {
                    // Install dependencies
                    bat 'pip install -r requirements.txt' // On Windows
                }
            }
        }
        stage('Run tests') {
            steps {
                script {
                    // Run tests
                    bat 'make test' // On Windows
                }
            }
        }
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                script {
                    // Deploy only if the branch is 'main'
                    bat 'make deploy' // On Windows
                }
            }
        }
    }
}
