// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ur_dashboard_msgs:srv/GetLoadedProgram.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "ur_dashboard_msgs/srv/get_loaded_program.hpp"


#ifndef UR_DASHBOARD_MSGS__SRV__DETAIL__GET_LOADED_PROGRAM__BUILDER_HPP_
#define UR_DASHBOARD_MSGS__SRV__DETAIL__GET_LOADED_PROGRAM__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ur_dashboard_msgs/srv/detail/get_loaded_program__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ur_dashboard_msgs
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ur_dashboard_msgs::srv::GetLoadedProgram_Request>()
{
  return ::ur_dashboard_msgs::srv::GetLoadedProgram_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace ur_dashboard_msgs


namespace ur_dashboard_msgs
{

namespace srv
{

namespace builder
{

class Init_GetLoadedProgram_Response_success
{
public:
  explicit Init_GetLoadedProgram_Response_success(::ur_dashboard_msgs::srv::GetLoadedProgram_Response & msg)
  : msg_(msg)
  {}
  ::ur_dashboard_msgs::srv::GetLoadedProgram_Response success(::ur_dashboard_msgs::srv::GetLoadedProgram_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ur_dashboard_msgs::srv::GetLoadedProgram_Response msg_;
};

class Init_GetLoadedProgram_Response_program_name
{
public:
  explicit Init_GetLoadedProgram_Response_program_name(::ur_dashboard_msgs::srv::GetLoadedProgram_Response & msg)
  : msg_(msg)
  {}
  Init_GetLoadedProgram_Response_success program_name(::ur_dashboard_msgs::srv::GetLoadedProgram_Response::_program_name_type arg)
  {
    msg_.program_name = std::move(arg);
    return Init_GetLoadedProgram_Response_success(msg_);
  }

private:
  ::ur_dashboard_msgs::srv::GetLoadedProgram_Response msg_;
};

class Init_GetLoadedProgram_Response_answer
{
public:
  Init_GetLoadedProgram_Response_answer()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GetLoadedProgram_Response_program_name answer(::ur_dashboard_msgs::srv::GetLoadedProgram_Response::_answer_type arg)
  {
    msg_.answer = std::move(arg);
    return Init_GetLoadedProgram_Response_program_name(msg_);
  }

private:
  ::ur_dashboard_msgs::srv::GetLoadedProgram_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ur_dashboard_msgs::srv::GetLoadedProgram_Response>()
{
  return ur_dashboard_msgs::srv::builder::Init_GetLoadedProgram_Response_answer();
}

}  // namespace ur_dashboard_msgs


namespace ur_dashboard_msgs
{

namespace srv
{

namespace builder
{

class Init_GetLoadedProgram_Event_response
{
public:
  explicit Init_GetLoadedProgram_Event_response(::ur_dashboard_msgs::srv::GetLoadedProgram_Event & msg)
  : msg_(msg)
  {}
  ::ur_dashboard_msgs::srv::GetLoadedProgram_Event response(::ur_dashboard_msgs::srv::GetLoadedProgram_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ur_dashboard_msgs::srv::GetLoadedProgram_Event msg_;
};

class Init_GetLoadedProgram_Event_request
{
public:
  explicit Init_GetLoadedProgram_Event_request(::ur_dashboard_msgs::srv::GetLoadedProgram_Event & msg)
  : msg_(msg)
  {}
  Init_GetLoadedProgram_Event_response request(::ur_dashboard_msgs::srv::GetLoadedProgram_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_GetLoadedProgram_Event_response(msg_);
  }

private:
  ::ur_dashboard_msgs::srv::GetLoadedProgram_Event msg_;
};

class Init_GetLoadedProgram_Event_info
{
public:
  Init_GetLoadedProgram_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GetLoadedProgram_Event_request info(::ur_dashboard_msgs::srv::GetLoadedProgram_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_GetLoadedProgram_Event_request(msg_);
  }

private:
  ::ur_dashboard_msgs::srv::GetLoadedProgram_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ur_dashboard_msgs::srv::GetLoadedProgram_Event>()
{
  return ur_dashboard_msgs::srv::builder::Init_GetLoadedProgram_Event_info();
}

}  // namespace ur_dashboard_msgs

#endif  // UR_DASHBOARD_MSGS__SRV__DETAIL__GET_LOADED_PROGRAM__BUILDER_HPP_
