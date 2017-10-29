From mathcomp.ssreflect
Require Import ssreflect ssrbool ssrnat eqtype ssrfun seq.


(* Definition nid := nat. *)
(* Definition data := seq nid. *)

(* (* Proposer states *) *)
(* Inductive PState := *)
(* (* Waiting at a current stage *) *)
(* | PInit *)
(* (* Sent prepare message to some Acceptors at a current stage *)          *)
(* | PSentPrep of data & seq nid *)
(* (* Received results from some Acceptors, bool for promise/NACK *) *)
(* | PWaitPrepResponse of data & seq (nid * bool) *)
(* (* Send AcceptRequest *) *)
(* | PSentAccReq of data & seq nid *)
(* (* Waiting for acks on AcceptRequest with some already collected *) *)
(* | PWaitAckReqResp of data & seq nid. *)

(* (* Acceptor states *) *)
(* Inductive AState := *)
(* (* Waiting at a current stage *) *)
(* | AInit *)
(* | AGotPrep of data *)
(* | ASentPromise | ASentNACK *)
(* | AGotAccReq of data *)
(* | ASentAccepted of data. *)


Record Proposal :=
  mkProposal {
      no: nat;
      value: nat;
      isNack: bool;
    }.

Record Proposer :=
  mkProposer {
    p_no: nat;
    p_val: nat;
  }.

Record Acceptor :=
  mkAcceptor {
      promised_no: nat;
      accepted_proposal: Proposal; 
    }.


Definition nack := mkProposal 0 0 true.
(* Don't know if NACK can be implemented as an higher order type or
 something so that we can easily return it from any function *)


(* returns a pair containing the new acceptor state plus an accepted proposal if any otherwise NACK*)
Definition prepare (proposal_no: nat) (a: Acceptor) :=
  if proposal_no > promised_no a
  then
    let: new_a := mkAcceptor proposal_no (accepted_proposal a) in
    pair new_a (accepted_proposal a)
  else
    pair a nack. (* Send NACK  *)

Fixpoint send_prepare (p: Proposer) (acceptors: seq Acceptor) :=
  let: proposal_no := p_no p in
  match acceptors with
  | nil => nil
  | a :: rest => (prepare proposal_no a) :: send_prepare p rest
  end.

(* Returns the new state of the Acceptor *)
Definition accept_request (p: Proposal) (a: Acceptor) :=
  if no p >= promised_no a
  then
    (* TODO: function to inform learner *)
    mkAcceptor (promised_no a) p
  else a.

Fixpoint send_accept_request (p: Proposer) (acceptors: seq Acceptor) :=
  (* TODO: Function to check if accept_request can be sent *)
  let: proposal := mkProposal (p_no p) (p_val p) false in
  match acceptors with
  | nil => nil
  | a :: rest => (accept_request proposal a) :: send_accept_request p rest
  end.
