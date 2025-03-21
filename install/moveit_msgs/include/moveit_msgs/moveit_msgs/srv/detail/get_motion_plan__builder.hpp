// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from moveit_msgs:srv/GetMotionPlan.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "moveit_msgs/srv/get_motion_plan.hpp"


#ifndef MOVEIT_MSGS__SRV__DETAIL__GET_MOTION_PLAN__BUILDER_HPP_
#define MOVEIT_MSGS__SRV__DETAIL__GET_MOTION_PLAN__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "moveit_msgs/srv/detail/get_motion_plan__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace moveit_msgs
{

namespace srv
{

namespace builder
{

class Init_GetMotionPlan_Request_motion_plan_request
{
public:
  Init_GetMotionPlan_Request_motion_plan_request()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::moveit_msgs::srv::GetMotionPlan_Request motion_plan_request(::moveit_msgs::srv::GetMotionPlan_Request::_motion_plan_request_type arg)
  {
    msg_.motion_plan_request = std::move(arg);
    return std::move(msg_);
  }

private:
  ::moveit_msgs::srv::GetMotionPlan_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::moveit_msgs::srv::GetMotionPlan_Request>()
{
  return moveit_msgs::srv::builder::Init_GetMotionPlan_Request_motion_plan_request();
}

}  // namespace moveit_msgs


namespace moveit_msgs
{

namespace srv
{

namespace builder
{

class Init_GetMotionPlan_Response_motion_plan_response
{
public:
  Init_GetMotionPlan_Response_motion_plan_response()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::moveit_msgs::srv::GetMotionPlan_Response motion_plan_response(::moveit_msgs::srv::GetMotionPlan_Response::_motion_plan_response_type arg)
  {
    msg_.motion_plan_response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::moveit_msgs::srv::GetMotionPlan_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::moveit_msgs::srv::GetMotionPlan_Response>()
{
  return moveit_msgs::srv::builder::Init_GetMotionPlan_Response_motion_plan_response();
}

}  // namespace moveit_msgs


namespace moveit_msgs
{

namespace srv
{

namespace builder
{

class Init_GetMotionPlan_Event_response
{
public:
  explicit Init_GetMotionPlan_Event_response(::moveit_msgs::srv::GetMotionPlan_Event & msg)
  : msg_(msg)
  {}
  ::moveit_msgs::srv::GetMotionPlan_Event response(::moveit_msgs::srv::GetMotionPlan_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::moveit_msgs::srv::GetMotionPlan_Event msg_;
};

class Init_GetMotionPlan_Event_request
{
public:
  explicit Init_GetMotionPlan_Event_request(::moveit_msgs::srv::GetMotionPlan_Event & msg)
  : msg_(msg)
  {}
  Init_GetMotionPlan_Event_response request(::moveit_msgs::srv::GetMotionPlan_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_GetMotionPlan_Event_response(msg_);
  }

private:
  ::moveit_msgs::srv::GetMotionPlan_Event msg_;
};

class Init_GetMotionPlan_Event_info
{
public:
  Init_GetMotionPlan_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GetMotionPlan_Event_request info(::moveit_msgs::srv::GetMotionPlan_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_GetMotionPlan_Event_request(msg_);
  }

private:
  ::moveit_msgs::srv::GetMotionPlan_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::moveit_msgs::srv::GetMotionPlan_Event>()
{
  return moveit_msgs::srv::builder::Init_GetMotionPlan_Event_info();
}

}  // namespace moveit_msgs

#endif  // MOVEIT_MSGS__SRV__DETAIL__GET_MOTION_PLAN__BUILDER_HPP_
