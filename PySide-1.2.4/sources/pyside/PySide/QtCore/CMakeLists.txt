project(QtCore)

set(QtCore_gluecode "${CMAKE_CURRENT_SOURCE_DIR}/glue/qeasingcurve_glue.cpp")

if (${QT_VERSION_MAJOR} EQUAL 4 AND ${QT_VERSION_MINOR} LESS 6)
    set (QtCore_46_SRC )
else()
    set(QtCore_46_SRC
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qeasingcurve_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qabstractanimation_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qabstractstate_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qabstracttransition_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qanimationgroup_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qeventtransition_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qfinalstate_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qhistorystate_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qmargins_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qparallelanimationgroup_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qpauseanimation_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qprocessenvironment_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qpropertyanimation_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qsequentialanimationgroup_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qsignaltransition_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qstate_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qstatemachine_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qstatemachine_signalevent_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qstatemachine_wrappedevent_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qvariantanimation_wrapper.cpp
    )
endif()
if (${QT_VERSION_MAJOR} EQUAL 4 AND ${QT_VERSION_MINOR} LESS 7)
    set (QtCore_47_SRC )
else()
    set(QtCore_47_SRC
    ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/qelapsedtimer_wrapper.cpp
    )
endif()

if(ENABLE_WIN)
    set(SPECIFIC_OS_FILES
        ${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/msg_wrapper.cpp
        ${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/point_wrapper.cpp
    )
else()
    set(SPECIFIC_OS_FILES "")
endif()

set(QtCore_SRC
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qabstracteventdispatcher_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qabstractfileengine_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qabstractfileenginehandler_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qabstractfileengineiterator_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qabstractitemmodel_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qabstractlistmodel_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qabstracttablemodel_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qbasictimer_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qbitarray_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qbuffer_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qbytearray_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qbytearraymatcher_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qchildevent_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qcoreapplication_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qcryptographichash_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qdatastream_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qdate_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qdatetime_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qdir_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qdiriterator_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qdynamicpropertychangeevent_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qevent_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qeventloop_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qfactoryinterface_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qfile_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qfileinfo_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qfilesystemwatcher_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qfsfileengine_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qgenericargument_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qgenericreturnargument_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qiodevice_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qlibraryinfo_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qline_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qlinef_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qlocale_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qmetaclassinfo_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qmetaenum_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qmetaproperty_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qmetamethod_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qmetaobject_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qmimedata_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qmodelindex_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qmutex_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qmutexlocker_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qobject_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qpersistentmodelindex_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qpluginloader_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qpoint_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qpointf_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qprocess_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qreadlocker_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qreadwritelock_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qrect_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qrectf_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qregexp_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qresource_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qrunnable_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qsemaphore_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qsettings_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qsignalmapper_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qsize_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qsizef_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qsocketnotifier_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qsysinfo_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qsystemlocale_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qsystemsemaphore_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qt_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qtconcurrent_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qtcore_module_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qtemporaryfile_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qtextboundaryfinder_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qtextcodec_converterstate_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qtextcodec_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qtextdecoder_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qtextencoder_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qtextstream_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qtextstreammanipulator_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qthread_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qthreadpool_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qtime_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qtimeline_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qtimer_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qtimerevent_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qtranslator_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qurl_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/quuid_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qwaitcondition_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qwritelocker_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qxmlstreamattribute_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qxmlstreamattributes_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qxmlstreamentitydeclaration_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qxmlstreamentityresolver_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qxmlstreamnamespacedeclaration_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qxmlstreamnotationdeclaration_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qxmlstreamreader_wrapper.cpp
${CMAKE_CURRENT_BINARY_DIR}/PySide/QtCore/qxmlstreamwriter_wrapper.cpp
${QtCore_46_SRC}
${QtCore_47_SRC}
${SPECIFIC_OS_FILES}
)

configure_file("${CMAKE_CURRENT_SOURCE_DIR}/typesystem_core.xml.in"
               "${CMAKE_CURRENT_BINARY_DIR}/typesystem_core.xml" @ONLY)

set(QtCore_typesystem_path "${QtCore_SOURCE_DIR}")

set(QtCore_include_dirs ${CMAKE_CURRENT_SOURCE_DIR}
                        ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/QtCore/
                        ${QT_INCLUDE_DIR}
                        ${SHIBOKEN_INCLUDE_DIR}
                        ${libpyside_SOURCE_DIR}
                        ${SHIBOKEN_PYTHON_INCLUDE_DIR})
set(QtCore_libraries  pyside
                      ${SHIBOKEN_PYTHON_LIBRARIES}
                      ${SHIBOKEN_LIBRARY}
                      ${QT_QTCORE_LIBRARY})

create_pyside_module(QtCore
                     QtCore_include_dirs
                     QtCore_libraries
                     ""
                     QtCore_typesystem_path
                     QtCore_SRC
                     QtCore_gluecode
                     ${CMAKE_CURRENT_BINARY_DIR}/typesystem_core.xml)
