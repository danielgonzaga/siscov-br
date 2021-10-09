import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RioGrandeDoSulComponent } from './rio-grande-do-sul.component';

describe('RioGrandeDoSulComponent', () => {
  let component: RioGrandeDoSulComponent;
  let fixture: ComponentFixture<RioGrandeDoSulComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RioGrandeDoSulComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RioGrandeDoSulComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
