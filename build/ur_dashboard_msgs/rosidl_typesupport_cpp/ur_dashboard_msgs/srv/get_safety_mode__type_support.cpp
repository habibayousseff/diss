// generated from rosidl_typesupport_cpp/resource/idl__type_support.cpp.em
// with input from ur_dashboard_msgs:srv/GetSafetyMode.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "ur_dashboard_msgs/srv/detail/get_safety_mode__functions.h"
#include "ur_dashboard_msgs/srv/detail/get_safety_mode__struct.hpp"
#include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
#include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace ur_dashboard_msgs
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _GetSafetyMode_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _GetSafetyMode_Request_type_support_ids_t;

static const _GetSafetyMode_Request_type_support_ids_t _GetSafetyMode_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _GetSafetyMode_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _GetSafetyMode_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _GetSafetyMode_Request_type_support_symbol_names_t _GetSafetyMode_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ur_dashboard_msgs, srv, GetSafetyMode_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ur_dashboard_msgs, srv, GetSafetyMode_Request)),
  }
};

typedef struct _GetSafetyMode_Request_type_support_data_t
{
  void * data[2];
} _GetSafetyMode_Request_type_support_data_t;

static _GetSafetyMode_Request_type_support_data_t _GetSafetyMode_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _GetSafetyMode_Request_message_typesupport_map = {
  2,
  "ur_dashboard_msgs",
  &_GetSafetyMode_Request_message_typesupport_ids.typesupport_identifier[0],
  &_GetSafetyMode_Request_message_typesupport_symbol_names.symbol_name[0],
  &_GetSafetyMode_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t GetSafetyMode_Request_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_GetSafetyMode_Request_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
  &ur_dashboard_msgs__srv__GetSafetyMode_Request__get_type_hash,
  &ur_dashboard_msgs__srv__GetSafetyMode_Request__get_type_description,
  &ur_dashboard_msgs__srv__GetSafetyMode_Request__get_type_description_sources,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace ur_dashboard_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ur_dashboard_msgs::srv::GetSafetyMode_Request>()
{
  return &::ur_dashboard_msgs::srv::rosidl_typesupport_cpp::GetSafetyMode_Request_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, ur_dashboard_msgs, srv, GetSafetyMode_Request)() {
  return get_message_type_support_handle<ur_dashboard_msgs::srv::GetSafetyMode_Request>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "ur_dashboard_msgs/srv/detail/get_safety_mode__functions.h"
// already included above
// #include "ur_dashboard_msgs/srv/detail/get_safety_mode__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace ur_dashboard_msgs
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _GetSafetyMode_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _GetSafetyMode_Response_type_support_ids_t;

static const _GetSafetyMode_Response_type_support_ids_t _GetSafetyMode_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _GetSafetyMode_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _GetSafetyMode_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _GetSafetyMode_Response_type_support_symbol_names_t _GetSafetyMode_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ur_dashboard_msgs, srv, GetSafetyMode_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ur_dashboard_msgs, srv, GetSafetyMode_Response)),
  }
};

typedef struct _GetSafetyMode_Response_type_support_data_t
{
  void * data[2];
} _GetSafetyMode_Response_type_support_data_t;

static _GetSafetyMode_Response_type_support_data_t _GetSafetyMode_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _GetSafetyMode_Response_message_typesupport_map = {
  2,
  "ur_dashboard_msgs",
  &_GetSafetyMode_Response_message_typesupport_ids.typesupport_identifier[0],
  &_GetSafetyMode_Response_message_typesupport_symbol_names.symbol_name[0],
  &_GetSafetyMode_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t GetSafetyMode_Response_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_GetSafetyMode_Response_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
  &ur_dashboard_msgs__srv__GetSafetyMode_Response__get_type_hash,
  &ur_dashboard_msgs__srv__GetSafetyMode_Response__get_type_description,
  &ur_dashboard_msgs__srv__GetSafetyMode_Response__get_type_description_sources,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace ur_dashboard_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ur_dashboard_msgs::srv::GetSafetyMode_Response>()
{
  return &::ur_dashboard_msgs::srv::rosidl_typesupport_cpp::GetSafetyMode_Response_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, ur_dashboard_msgs, srv, GetSafetyMode_Response)() {
  return get_message_type_support_handle<ur_dashboard_msgs::srv::GetSafetyMode_Response>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "ur_dashboard_msgs/srv/detail/get_safety_mode__functions.h"
// already included above
// #include "ur_dashboard_msgs/srv/detail/get_safety_mode__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace ur_dashboard_msgs
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _GetSafetyMode_Event_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _GetSafetyMode_Event_type_support_ids_t;

static const _GetSafetyMode_Event_type_support_ids_t _GetSafetyMode_Event_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _GetSafetyMode_Event_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _GetSafetyMode_Event_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _GetSafetyMode_Event_type_support_symbol_names_t _GetSafetyMode_Event_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ur_dashboard_msgs, srv, GetSafetyMode_Event)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ur_dashboard_msgs, srv, GetSafetyMode_Event)),
  }
};

typedef struct _GetSafetyMode_Event_type_support_data_t
{
  void * data[2];
} _GetSafetyMode_Event_type_support_data_t;

static _GetSafetyMode_Event_type_support_data_t _GetSafetyMode_Event_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _GetSafetyMode_Event_message_typesupport_map = {
  2,
  "ur_dashboard_msgs",
  &_GetSafetyMode_Event_message_typesupport_ids.typesupport_identifier[0],
  &_GetSafetyMode_Event_message_typesupport_symbol_names.symbol_name[0],
  &_GetSafetyMode_Event_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t GetSafetyMode_Event_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_GetSafetyMode_Event_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
  &ur_dashboard_msgs__srv__GetSafetyMode_Event__get_type_hash,
  &ur_dashboard_msgs__srv__GetSafetyMode_Event__get_type_description,
  &ur_dashboard_msgs__srv__GetSafetyMode_Event__get_type_description_sources,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace ur_dashboard_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ur_dashboard_msgs::srv::GetSafetyMode_Event>()
{
  return &::ur_dashboard_msgs::srv::rosidl_typesupport_cpp::GetSafetyMode_Event_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, ur_dashboard_msgs, srv, GetSafetyMode_Event)() {
  return get_message_type_support_handle<ur_dashboard_msgs::srv::GetSafetyMode_Event>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "ur_dashboard_msgs/srv/detail/get_safety_mode__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/service_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace ur_dashboard_msgs
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _GetSafetyMode_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _GetSafetyMode_type_support_ids_t;

static const _GetSafetyMode_type_support_ids_t _GetSafetyMode_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _GetSafetyMode_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _GetSafetyMode_type_support_symbol_names_t;
#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _GetSafetyMode_type_support_symbol_names_t _GetSafetyMode_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ur_dashboard_msgs, srv, GetSafetyMode)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ur_dashboard_msgs, srv, GetSafetyMode)),
  }
};

typedef struct _GetSafetyMode_type_support_data_t
{
  void * data[2];
} _GetSafetyMode_type_support_data_t;

static _GetSafetyMode_type_support_data_t _GetSafetyMode_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _GetSafetyMode_service_typesupport_map = {
  2,
  "ur_dashboard_msgs",
  &_GetSafetyMode_service_typesupport_ids.typesupport_identifier[0],
  &_GetSafetyMode_service_typesupport_symbol_names.symbol_name[0],
  &_GetSafetyMode_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t GetSafetyMode_service_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_GetSafetyMode_service_typesupport_map),
  ::rosidl_typesupport_cpp::get_service_typesupport_handle_function,
  ::rosidl_typesupport_cpp::get_message_type_support_handle<ur_dashboard_msgs::srv::GetSafetyMode_Request>(),
  ::rosidl_typesupport_cpp::get_message_type_support_handle<ur_dashboard_msgs::srv::GetSafetyMode_Response>(),
  ::rosidl_typesupport_cpp::get_message_type_support_handle<ur_dashboard_msgs::srv::GetSafetyMode_Event>(),
  &::rosidl_typesupport_cpp::service_create_event_message<ur_dashboard_msgs::srv::GetSafetyMode>,
  &::rosidl_typesupport_cpp::service_destroy_event_message<ur_dashboard_msgs::srv::GetSafetyMode>,
  &ur_dashboard_msgs__srv__GetSafetyMode__get_type_hash,
  &ur_dashboard_msgs__srv__GetSafetyMode__get_type_description,
  &ur_dashboard_msgs__srv__GetSafetyMode__get_type_description_sources,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace ur_dashboard_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<ur_dashboard_msgs::srv::GetSafetyMode>()
{
  return &::ur_dashboard_msgs::srv::rosidl_typesupport_cpp::GetSafetyMode_service_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_cpp, ur_dashboard_msgs, srv, GetSafetyMode)() {
  return ::rosidl_typesupport_cpp::get_service_type_support_handle<ur_dashboard_msgs::srv::GetSafetyMode>();
}

#ifdef __cplusplus
}
#endif
