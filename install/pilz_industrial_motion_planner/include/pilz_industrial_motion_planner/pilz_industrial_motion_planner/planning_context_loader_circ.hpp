/*********************************************************************
 * Software License Agreement (BSD License)
 *
 *  Copyright (c) 2018 Pilz GmbH & Co. KG
 *  All rights reserved.
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions
 *  are met:
 *
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above
 *     copyright notice, this list of conditions and the following
 *     disclaimer in the documentation and/or other materials provided
 *     with the distribution.
 *   * Neither the name of Pilz GmbH & Co. KG nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 *  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 *  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 *  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 *  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 *  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 *  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 *  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 *  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 *  POSSIBILITY OF SUCH DAMAGE.
 *********************************************************************/

#pragma once

#include <pilz_industrial_motion_planner/planning_context_loader.hpp>

#include <moveit/planning_interface/planning_interface.hpp>

namespace pilz_industrial_motion_planner
{
/**
 * @brief Plugin that can generate instances of PlanningContextCIRC.
 * Generates instances of PlanningContextLIN.
 */
class PlanningContextLoaderCIRC : public PlanningContextLoader
{
public:
  PlanningContextLoaderCIRC();
  ~PlanningContextLoaderCIRC() override;

  /**
   * @brief return a instance of
   * pilz_industrial_motion_planner::PlanningContextCIRC
   * @param planning_context returned context
   * @param name
   * @param group
   * @return true on success, false otherwise
   */
  bool loadContext(planning_interface::PlanningContextPtr& planning_context, const std::string& name,
                   const std::string& group) const override;
};

typedef std::shared_ptr<PlanningContextLoaderCIRC> PlanningContextLoaderCIRCPtr;
typedef std::shared_ptr<const PlanningContextLoaderCIRC> PlanningContextLoaderCIRCConstPtr;

}  // namespace pilz_industrial_motion_planner
