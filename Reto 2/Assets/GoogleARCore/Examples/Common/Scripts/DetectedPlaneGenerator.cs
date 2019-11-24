//-----------------------------------------------------------------------
// <copyright file="DetectedPlaneGenerator.cs" company="Google">
//
// Copyright 2018 Google Inc. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
// </copyright>
//-----------------------------------------------------------------------

namespace GoogleARCore.Examples.Common
{
    using System.Collections.Generic;
    using GoogleARCore;
    using UnityEngine;
    using UnityEngine.UI;

    /// <summary>
    /// Manages the visualization of detected planes in the scene.
    /// </summary>
    public class DetectedPlaneGenerator : MonoBehaviour
    {
        /// <summary>
        /// A prefab for tracking and visualizing detected planes.
        /// </summary>
        public GameObject DetectedPlanePrefab;
        public Renderer DetectedPlanePrefabMaterial;
        public Material originalMaterial;
        public Material blueMaterial;
        public Material orangeMaterial;
        public Material greenMaterial;
        public Button originalButton;
        public Button blueButton;
        public Button orangeButton;
        public Button greenButton;
        private List<GameObject> planes = new List<GameObject>();

        /// <summary>
        /// A list to hold new planes ARCore began tracking in the current frame. This object is
        /// used across the application to avoid per-frame allocations.
        /// </summary>
        private List<DetectedPlane> m_NewPlanes = new List<DetectedPlane>();

        /// <summary>
        /// The Unity Update method.
        /// </summary>

        public void Start()
        {
            originalButton.onClick.AddListener(_OnOriginalButtonClicked);
            blueButton.onClick.AddListener(_OnBlueButtonClicked);
            orangeButton.onClick.AddListener(_OnOrangeButtonClicked);
            greenButton.onClick.AddListener(_OnGreenButtonClicked);
        }
        public void Update()
        {
            // Check that motion tracking is tracking.
            if (Session.Status != SessionStatus.Tracking)
            {
                return;
            }

            // Iterate over planes found in this frame and instantiate corresponding GameObjects to
            // visualize them.
            Session.GetTrackables<DetectedPlane>(m_NewPlanes, TrackableQueryFilter.New);
            for (int i = 0; i < m_NewPlanes.Count; i++)
            {
                // Instantiate a plane visualization prefab and set it to track the new plane. The
                // transform is set to the origin with an identity rotation since the mesh for our
                // prefab is updated in Unity World coordinates.
                if(m_NewPlanes[i].PlaneType==DetectedPlaneType.Vertical){
                    GameObject planeObject = Instantiate(DetectedPlanePrefab, Vector3.zero, Quaternion.identity, transform);
                    planeObject.GetComponent<DetectedPlaneVisualizer>().Initialize(m_NewPlanes[i]);
                    planes.Add(planeObject);
                }
            }
        }
        public void OnDestroy()
        {
            originalButton.onClick.RemoveListener(_OnOriginalButtonClicked);
            blueButton.onClick.RemoveListener(_OnBlueButtonClicked);
            orangeButton.onClick.RemoveListener(_OnOrangeButtonClicked);
            greenButton.onClick.RemoveListener(_OnGreenButtonClicked);
        }

        private void _OnOriginalButtonClicked()
        {
            foreach(GameObject plane in planes){
                plane.GetComponent<Renderer>().material = originalMaterial;
            }
            DetectedPlanePrefabMaterial.material = originalMaterial;
        }
        private void _OnBlueButtonClicked()
        {
            foreach(GameObject plane in planes){
                plane.GetComponent<Renderer>().material = blueMaterial;
            }
            DetectedPlanePrefabMaterial.material = blueMaterial;
        }
        private void _OnOrangeButtonClicked()
        {
            foreach(GameObject plane in planes){
                plane.GetComponent<Renderer>().material = orangeMaterial;
            }
            DetectedPlanePrefabMaterial.material = orangeMaterial;
        }
        private void _OnGreenButtonClicked()
        {
            foreach(GameObject plane in planes){
                plane.GetComponent<Renderer>().material = greenMaterial;
            }
            DetectedPlanePrefabMaterial.material = greenMaterial;
        }
    }
}
