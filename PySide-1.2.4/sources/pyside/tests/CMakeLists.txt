if(CMAKE_VERSION VERSION_LESS 2.8)
    message("CMake version greater than 2.8 necessary to run tests")
else()
    if(NOT CTEST_TESTING_TIMEOUT)
        set(CTEST_TESTING_TIMEOUT 60)
    endif()

   if(WIN32)
        set(TEST_PYTHONPATH     "${CMAKE_BINARY_DIR};${CMAKE_SOURCE_DIR}/tests/util;${pysidetest_BINARY_DIR};$ENV{PYTHONPATH}")
        set(TEST_LIBRARY_PATH   "${libpyside_BINARY_DIR};${pysidetest_BINARY_DIR};${SHIBOKEN_INCLUDE_DIR}/../../bin;$ENV{PATH}")
        set(LIBRARY_PATH_VAR    "PATH")
        string(REPLACE "\\" "/" TEST_PYTHONPATH "${TEST_PYTHONPATH}")
        string(REPLACE "\\" "/" TEST_LIBRARY_PATH "${TEST_LIBRARY_PATH}")

        string(REPLACE ";" "\\;" TEST_PYTHONPATH "${TEST_PYTHONPATH}")
        string(REPLACE ";" "\\;" TEST_LIBRARY_PATH "${TEST_LIBRARY_PATH}")
    else()
        set(TEST_PYTHONPATH     "${CMAKE_BINARY_DIR}:${CMAKE_SOURCE_DIR}/tests/util:${pysidetest_BINARY_DIR}:$ENV{PYTHONPATH}")
        set(TEST_LIBRARY_PATH   "${libpyside_BINARY_DIR}:${pysidetest_BINARY_DIR}:$ENV{LD_LIBRARY_PATH}")
        set(LIBRARY_PATH_VAR    "LD_LIBRARY_PATH")
    endif()


    macro(TEST_QT_MODULE var name)
      if(NOT DISABLE_${name} AND ${var})
          add_subdirectory(${name})
      endif()
    endmacro()

    macro(PYSIDE_TEST)
        string(REGEX MATCH "/([^/]+)//?([^/]+)\\.py" foo "${CMAKE_CURRENT_SOURCE_DIR}/${ARGV0}" )
        set(TEST_NAME "${CMAKE_MATCH_1}_${CMAKE_MATCH_2}")
        if (${ARGC} EQUAL 1)
            set(EXPECT_TO_FAIL 0)
        elseif(${ARGC} EQUAL 2)
            set(EXPECT_TO_FAIL ${ARGV1})
        else()
            message(WARNING "Invalid call of macro PYSIDE_TEST")
        endif()
        set(TEST_CMD ${XVFB_EXEC} ${SHIBOKEN_PYTHON_INTERPRETER} "${CMAKE_CURRENT_SOURCE_DIR}/${ARGV0}")
        add_test(${TEST_NAME} ${TEST_CMD})
        set_tests_properties(${TEST_NAME} PROPERTIES
                             TIMEOUT ${CTEST_TESTING_TIMEOUT}
                             WILL_FAIL ${EXPECT_TO_FAIL}
                             ENVIRONMENT "PYTHONPATH=${TEST_PYTHONPATH};${LIBRARY_PATH_VAR}=${TEST_LIBRARY_PATH}")
    endmacro()

    # Try to find QtMultimedia
    # TODO: Remove this hack when cmake support QtMultimedia module
    if (NOT QT_QTMULTIMEDIA_FOUND AND ${QTVERSION} VERSION_GREATER 4.5.9)
        find_path(QT_QTMULTIMEDIA_INCLUDE_DIR QtMultimedia
                PATHS ${QT_HEADERS_DIR}/QtMultimedia
                    ${QT_LIBRARY_DIR}/QtMultimedia.framework/Headers
                NO_DEFAULT_PATH)
        find_library(QT_QTMULTIMEDIA_LIBRARY QtMultimedia PATHS ${QT_LIBRARY_DIR} NO_DEFAULT_PATH)
        if (QT_QTMULTIMEDIA_INCLUDE_DIR AND QT_QTMULTIMEDIA_LIBRARY)
            set(QT_QTMULTIMEDIA_FOUND ON)
        endif()
    endif ()

    add_subdirectory(pysidetest)
    add_subdirectory(signals)
    TEST_QT_MODULE(QT_QTCORE_FOUND QtCore)
    TEST_QT_MODULE(QT_QTGUI_FOUND QtGui)
    TEST_QT_MODULE(QT_QTNETWORK_FOUND QtNetwork)
    TEST_QT_MODULE(QT_QTWEBKIT_FOUND QtWebKit)
    TEST_QT_MODULE(QT_QTSVG_FOUND QtSvg)
    TEST_QT_MODULE(QT_QTXML_FOUND QtXml)
    TEST_QT_MODULE(QT_QTTEST_FOUND QtTest)
    TEST_QT_MODULE(QT_QTOPENGL_FOUND QtOpenGL)
    TEST_QT_MODULE(QT_QTSQL_FOUND QtSql)
    TEST_QT_MODULE(QT_QTUITOOLS_FOUND QtUiTools)
    TEST_QT_MODULE(QT_QTHELP_FOUND QtHelp)
    TEST_QT_MODULE(QT_QTXMLPATTERNS_FOUND QtXmlPatterns)
    TEST_QT_MODULE(QT_QTMAEMO5_FOUND QtMaemo5)
    TEST_QT_MODULE(QT_QTSCRIPT_FOUND QtScript)
    TEST_QT_MODULE(QT_QTSCRIPTTOOLS_FOUND QtScriptTools)
    TEST_QT_MODULE(QT_QTMULTIMEDIA_FOUND QtMultimedia)
    TEST_QT_MODULE(QT_PHONON_FOUND phonon)
    TEST_QT_MODULE(QT_QTDECLARATIVE_FOUND QtDeclarative)

    #platform specific
    if (ENABLE_MAC)
        add_subdirectory(mac)
    endif ()
endif()
