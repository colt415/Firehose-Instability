/**************************************************************************
 * Ideal MHD physics module for BOUT++
 * This version evolves the entire quantity (initial + perturbed)
 **************************************************************************/

#include <bout.hxx>
#include <boutmain.hxx>
#include <msg_stack.hxx>

//2D initial profile
Field2D rho0,Pperp0,Ppar0;
Vector2D v0,B0;

// 3D evolving variables
Field3D rho, Pperp, Ppar; // density, pressure
Vector3D v, B;  // velocity, magnetic field

//Field3D divB; // Divergence of B (for monitoring)

// parameters
//BoutReal gamma;
bool nonlinear;
//BoutReal viscos;

int physics_init(bool restarting) {
  // 2D initial profiles
//  Field2D rho0, p0;
//  Vector2D v0, B0;

  // read options
  Options *globalOptions = Options::getRoot();
  Options *options = globalOptions->getSection("firehose");
//  OPTION(options, gamma,          5.0/3.0);
//  OPTION(options, include_viscos, false);
  OPTION(options, nonlinear, false);
  
  // Read 2D initial profiles
  GRID_LOAD(rho0);
  GRID_LOAD(Pperp0);
  GRID_LOAD(Ppar0);
  v0.covariant = true; // Read covariant components of v0
  GRID_LOAD(v0);
  B0.covariant = false; // Read contravariant components of B0
  GRID_LOAD(B0);

  // tell BOUT which variables to evolve
  
  bout_solve(rho, "density");
  bout_solve(Pperp, "perppressure");
  bout_solve(Ppar, "parpressure");
  v.covariant = true; // evolve covariant components
  bout_solve(v, "v");
  B.covariant = false; // evolve contravariant components
  bout_solve(B, "B");

//  output.write("dx[0,0] = %e, dy[0,0] = %e, dz = %e\n", 
//	       mesh->dx[0][0], mesh->dy[0][0], mesh->dz);

//  dump.add(divB, "divB", 1);

//  divB.setBoundary("DivB");
  
//  divB.setBoundary("DivB"); // Set boundary conditions from options
  
/*  if(!restarting) {
    // Set variables to these values (+ the initial perturbation)
    // NOTE: This must be after the calls to bout_solve
    rho += rho0;
    p += p0;
    v += v0;
    B += B0;
  
    // Added this for modifying the Orszag-Tang vortex problem
    BoutReal v_fact;
    OPTION(options, v_fact, 1.0);
    v *= v_fact;

  }
*/
  return 0;
}

int physics_run(BoutReal t) {
  // Communicate variables
  mesh->communicate(v, B, Pperp, Ppar);
  mesh->communicate(rho);

//  msg_stack.push("F_rho");
//  ddt(rho)=0.0
  
  ddt(rho)=-rho0*Div(v);

//  msg_stack.pop(); msg_stack.push("F_p");

  ddt(Pperp) =0.0;
 
  ddt(Pperp)-=2*Pperp0*Div(v);//-Pperp0*B0*V_dot_Grad(B0,v);
  ddt(Pperp)+=Pperp0*B0*V_dot_Grad(B0,v);

  ddt(Ppar)=0.0;

  ddt(Ppar)-=Ppar0*Div(v);//+2*Ppar0*B0*V_dot_Grad(B0,v);
  ddt(Ppar)-=2*Ppar0*B0*V_dot_Grad(B0,v);

  
//  msg_stack.pop(); msg_stack.push("F_v");
 
  ddt(v) = 0.0;

  ddt(v)+=Curl(B)^B0/rho0;

  ddt(v)-=(V_dot_Grad(B0,Pperp)*B0-V_dot_Grad(B0,Ppar)*B0)/rho0;

  ddt(v)-=((Ppar0-Pperp0)*Div(B)*B0)/rho0;//+(Ppar0-Pperp0)*V_dot_Grad(B0,B))/rho;
  ddt(v)-=((Ppar0-Pperp0)*V_dot_Grad(B0,B))/rho0;
  ddt(v)-=Grad(Pperp)/rho0;
/*
  if(include_viscos) {
    ddt(v).x += viscos * Laplacian(v.x);
    ddt(v).y += viscos * Laplacian(v.y);
    ddt(v).z += viscos * Laplacian(v.z);
  }
  
  msg_stack.pop(); msg_stack.push("F_B");
  */
  ddt(B)=0.0;

  ddt(B)+= Curl(v^B0);

//  msg_stack.pop(); msg_stack.push("DivB");
//  divB=Div(B);

  return 0;
}
