import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-rio-grande-do-sul',
  templateUrl: './rio-grande-do-sul.component.html',
  styleUrls: ['./rio-grande-do-sul.component.css']
})
export class RioGrandeDoSulComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}
