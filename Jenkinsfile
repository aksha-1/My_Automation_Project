pipeline {

    agent any

    parameters {
        choice(name: 'ENV', choices: ['DEV', 'QA', 'STAGING'], description: 'Select Environment')
        choice(name: 'BROWSER', choices: ['chrome', 'edge'], description: 'Select Browser')
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/aksha-1/My_Automation_Project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
                bat 'pip install mysql-connector-python'
            }
        }

        stage('Run Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'UNSTABLE') {
                    bat """
                    pytest Test_cases ^
                    --browser=${params.BROWSER} ^
                    --env=${params.ENV} ^
                    --html=Reports/report.html ^
                    --self-contained-html ^
                    --junitxml=Reports/results.xml
                    """

                }
            }
        }

        stage('Publish Results') {
            steps {
                junit 'Reports/results.xml'
                archiveArtifacts artifacts: 'Reports/*', fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }

        success {
            echo 'All tests passed.'
        }

        unstable {
            echo 'Some tests failed. Please review the reports.'
        }

        failure {
            echo 'Pipeline failed due to a configuration or execution error.'
        }
    }
}