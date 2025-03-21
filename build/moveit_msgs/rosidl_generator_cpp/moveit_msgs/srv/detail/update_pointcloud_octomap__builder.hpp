// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from moveit_msgs:srv/UpdatePointcloudOctomap.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "moveit_msgs/srv/update_pointcloud_octomap.hpp"


#ifndef MOVEIT_MSGS__SRV__DETAIL__UPDATE_POINTCLOUD_OCTOMAP__BUILDER_HPP_
#define MOVEIT_MSGS__SRV__DETAIL__UPDATE_POINTCLOUD_OCTOMAP__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "moveit_msgs/srv/detail/update_pointcloud_octomap__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace moveit_msgs
{

namespace srv
{

namespace builder
{

class Init_UpdatePointcloudOctomap_Request_cloud
{
public:
  Init_UpdatePointcloudOctomap_Request_cloud()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::moveit_msgs::srv::UpdatePointcloudOctomap_Request cloud(::moveit_msgs::srv::UpdatePointcloudOctomap_Request::_cloud_type arg)
  {
    msg_.cloud = std::move(arg);
    return std::move(msg_);
  }

private:
  ::moveit_msgs::srv::UpdatePointcloudOctomap_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::moveit_msgs::srv::UpdatePointcloudOctomap_Request>()
{
  return moveit_msgs::srv::builder::Init_UpdatePointcloudOctomap_Request_cloud();
}

}  // namespace moveit_msgs


namespace moveit_msgs
{

namespace srv
{

namespace builder
{

class Init_UpdatePointcloudOctomap_Response_success
{
public:
  Init_UpdatePointcloudOctomap_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::moveit_msgs::srv::UpdatePointcloudOctomap_Response success(::moveit_msgs::srv::UpdatePointcloudOctomap_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::moveit_msgs::srv::UpdatePointcloudOctomap_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::moveit_msgs::srv::UpdatePointcloudOctomap_Response>()
{
  return moveit_msgs::srv::builder::Init_UpdatePointcloudOctomap_Response_success();
}

}  // namespace moveit_msgs


namespace moveit_msgs
{

namespace srv
{

namespace builder
{

class Init_UpdatePointcloudOctomap_Event_response
{
public:
  explicit Init_UpdatePointcloudOctomap_Event_response(::moveit_msgs::srv::UpdatePointcloudOctomap_Event & msg)
  : msg_(msg)
  {}
  ::moveit_msgs::srv::UpdatePointcloudOctomap_Event response(::moveit_msgs::srv::UpdatePointcloudOctomap_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::moveit_msgs::srv::UpdatePointcloudOctomap_Event msg_;
};

class Init_UpdatePointcloudOctomap_Event_request
{
public:
  explicit Init_UpdatePointcloudOctomap_Event_request(::moveit_msgs::srv::UpdatePointcloudOctomap_Event & msg)
  : msg_(msg)
  {}
  Init_UpdatePointcloudOctomap_Event_response request(::moveit_msgs::srv::UpdatePointcloudOctomap_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_UpdatePointcloudOctomap_Event_response(msg_);
  }

private:
  ::moveit_msgs::srv::UpdatePointcloudOctomap_Event msg_;
};

class Init_UpdatePointcloudOctomap_Event_info
{
public:
  Init_UpdatePointcloudOctomap_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_UpdatePointcloudOctomap_Event_request info(::moveit_msgs::srv::UpdatePointcloudOctomap_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_UpdatePointcloudOctomap_Event_request(msg_);
  }

private:
  ::moveit_msgs::srv::UpdatePointcloudOctomap_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::moveit_msgs::srv::UpdatePointcloudOctomap_Event>()
{
  return moveit_msgs::srv::builder::Init_UpdatePointcloudOctomap_Event_info();
}

}  // namespace moveit_msgs

#endif  // MOVEIT_MSGS__SRV__DETAIL__UPDATE_POINTCLOUD_OCTOMAP__BUILDER_HPP_
