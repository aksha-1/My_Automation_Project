pipeline {

    agent any

    parameters {

        choice(
            name: 'PLATFORM',
            choices: ['windows', 'linux'],
            description: 'Select Operating System'
        )

        choice(
            name: 'ENV',
            choices: ['DEV', 'QA', 'STAGING'],
            description: 'Select Environment'
        )

        choice(
            name: 'TEST_TYPE',
            choices: ['UI', 'API', 'ALL'],
            description: 'Select Test Type'
        )

        choice(
            name: 'BROWSER',
            choices: ['chrome', 'edge'],
            description: 'Select Browser (Applicable only for UI Tests)'
        )

        choice(
            name: 'SUITE',
            choices: ['all', 'smoke', 'regression', 'e2e'],
            description: 'Select Test Suite'
        )
    }

    stages {

        stage('Checkout') {

            steps {
                git 'https://github.com/aksha-1/My_Automation_Project.git'
            }

        }

        stage('Install Dependencies') {

            steps {

                script {

                    if (isUnix()) {

                        sh '''
                        python3 -m pip install --upgrade pip
                        pip3 install -r requirements.txt
                        '''

                    } else {

                        bat '''
                        python -m pip install --upgrade pip
                        pip install -r requirements.txt
                        '''

                    }

                }

            }

        }

        stage('Run Tests') {

            steps {

                catchError(buildResult: 'UNSTABLE', stageResult: 'UNSTABLE') {

                    script {

                        def suiteOption = ""
                        def testFolder = "Test_cases"

                        if (params.SUITE != "all") {
                            suiteOption = "-m ${params.SUITE}"
                        }

                        // Select test folder
                        if (params.TEST_TYPE == "UI") {

                            testFolder = "Test_cases/UI"

                        } else if (params.TEST_TYPE == "API") {

                            testFolder = "Test_cases/API"

                        } else {

                            testFolder = "Test_cases"

                        }

                        if (isUnix()) {

                            if (params.TEST_TYPE == "API") {

                                sh """
                                pytest ${testFolder} \
                                --env=${params.ENV} \
                                ${suiteOption} \
                                --html=Reports/report.html \
                                --self-contained-html \
                                --junitxml=Reports/results.xml
                                """

                            } else {

                                sh """
                                pytest ${testFolder} \
                                --browser=${params.BROWSER} \
                                --env=${params.ENV} \
                                ${suiteOption} \
                                --html=Reports/report.html \
                                --self-contained-html \
                                --junitxml=Reports/results.xml
                                """

                            }

                        } else {

                            if (params.TEST_TYPE == "API") {

                                bat """
                                pytest ${testFolder} ^
                                --env=${params.ENV} ^
                                ${suiteOption} ^
                                --html=Reports/report.html ^
                                --self-contained-html ^
                                --junitxml=Reports/results.xml
                                """

                            } else {

                                bat """
                                pytest ${testFolder} ^
                                --browser=${params.BROWSER} ^
                                --env=${params.ENV} ^
                                ${suiteOption} ^
                                --html=Reports/report.html ^
                                --self-contained-html ^
                                --junitxml=Reports/results.xml
                                """

                            }

                        }

                    }

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
            echo 'All tests passed successfully.'
        }

        unstable {
            echo 'Some tests failed. Please review the reports.'
        }

        failure {
            echo 'Pipeline failed due to configuration or execution issues.'
        }

    }

}

// pipeline {

//     agent  any

//     parameters {

//         choice(
//             name: 'PLATFORM',
//             choices: ['windows', 'linux'],
//             description: 'Select Operating System'
//         )

//         choice(
//             name: 'ENV',
//             choices: ['DEV', 'QA', 'STAGING'],
//             description: 'Select Environment'
//         )

//         choice(
//             name: 'BROWSER',
//             choices: ['chrome', 'edge'],
//             description: 'Select Browser'
//         )

//         choice(
//             name: 'SUITE',
//             choices: ['all', 'smoke', 'regression', 'e2e'],
//             description: 'Select Test Suite'
//         )
//     }

//     stages {

//         stage('Checkout') {
//             steps {
//                 git 'https://github.com/aksha-1/My_Automation_Project.git'
//             }
//         }

//         stage('Install Dependencies') {
//             steps {
//                 script {

//                     if (isUnix()) {

//                         sh '''
//                         python3 -m pip install --upgrade pip
//                         pip3 install -r requirements.txt
//                         '''

//                     } else {

//                         bat '''
//                         python -m pip install --upgrade pip
//                         pip install -r requirements.txt
//                         '''

//                     }

//                 }
//             }
//         }

//         stage('Run Tests') {

//             steps {

//                 catchError(buildResult: 'UNSTABLE', stageResult: 'UNSTABLE') {

//                     script {

//                         def suiteOption = ""

//                         if (params.SUITE != "all") {
//                             suiteOption = "-m ${params.SUITE}"
//                         }

//                         if (isUnix()) {

//                             sh """
//                             pytest Test_cases \
//                             --browser=${params.BROWSER} \
//                             --env=${params.ENV} \
//                             ${suiteOption} \
//                             --html=Reports/report.html \
//                             --self-contained-html \
//                             --junitxml=Reports/results.xml
//                             """

//                         } else {

//                             bat """
//                             pytest Test_cases ^
//                             --browser=${params.BROWSER} ^
//                             --env=${params.ENV} ^
//                             ${suiteOption} ^
//                             --html=Reports/report.html ^
//                             --self-contained-html ^
//                             --junitxml=Reports/results.xml
//                             """

//                         }

//                     }
//                 }
//             }
//         }

//         stage('Publish Results') {

//             steps {

//                 junit 'Reports/results.xml'

//                 archiveArtifacts artifacts: 'Reports/*', fingerprint: true

//             }
//         }

//     }

//     post {

//         always {
//             echo 'Pipeline execution completed.'
//         }

//         success {
//             echo 'All tests passed successfully.'
//         }

//         unstable {
//             echo 'Some tests failed. Please review the reports.'
//         }

//         failure {
//             echo 'Pipeline failed due to configuration or execution issues.'
//         }

//     }

// }